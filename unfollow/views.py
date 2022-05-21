from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_api_key.permissions import HasAPIKey

import json
from datetime import datetime, timedelta
from twitter_api.twitter_api import TwitterAPI
# Create your views here.
from .models import TwitterAccount, FollowingRelationship
from .serializers import TwitterAccountSerializer
import pytz

utc=pytz.UTC

# Create your views here.
class TwitterAccountList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TwitterAccount.objects.all()
    serializer_class = TwitterAccountSerializer


class TwitterAccountDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TwitterAccount.objects.all()
    serializer_class = TwitterAccountSerializer
def sortKeyFunctionLastTweetDate(e):
  return e['last_tweet_date']

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
@permission_classes([HasAPIKey])
def get_users_logged_in_user_is_following(request):
    body = json.loads(request.body)
    token = body['token']
    #
    twitter_api = TwitterAPI()
    twitter_id_to_check = body['twitter_id']
    current_user = TwitterAccount.objects.filter(twitter_id=twitter_id_to_check).first()
    accounts = []
    if not current_user:
        user_data = twitter_api.lookup_user(twitter_id=twitter_id_to_check)
        if not user_data:
            return Response("No twitter account with that id", status=404)
        current_user = TwitterAccount(twitter_id=twitter_id_to_check, twitter_username=user_data.username,
                                      twitter_name=user_data.name)
        print(current_user)
        current_user.save()
    followers = twitter_api.get_following_for_user(twitter_id=twitter_id_to_check, token=token)
    for user in followers:
        print(user.id)
        most_recent_tweet = twitter_api.get_most_recent_tweet_for_user(user.id, token=token)
        twitter_account = TwitterAccount.objects.filter(twitter_id=user.id).first()
        if not twitter_account:
            if most_recent_tweet is not None:
                twitter_account = TwitterAccount(twitter_id=user.id, twitter_username=user.username, twitter_name=user.name,
                                                last_tweet_date=most_recent_tweet.created_at)
                twitter_account.save()
                serializer = TwitterAccountSerializer(twitter_account)
                accounts.append(serializer.data)
                relationship = FollowingRelationship.objects.filter(twitter_user=current_user,
                                                                    follows=twitter_account).first()
                if not relationship:
                    relationship = FollowingRelationship(twitter_user=current_user, follows=twitter_account)
                    relationship.save()
            else:
                print(user.name)
        else:
            relationship = FollowingRelationship.objects.filter(twitter_user=current_user,
                                                                follows=twitter_account).first()
            if not relationship:
                relationship = FollowingRelationship(twitter_user=current_user, follows=twitter_account)
                relationship.save()

    return Response({"status": "success"})

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
@permission_classes([HasAPIKey])
def get_followers_whose_last_tweet_was_more_than_3_months_ago(request):
    body = json.loads(request.body)
    twitter_id_to_check = body['twitter_id']
    date_to_compare_against = utc.localize(datetime.now() - timedelta(days=90))
    results = []
    current_user = TwitterAccount.objects.filter(twitter_id=twitter_id_to_check).first()
    relationships = FollowingRelationship.objects.filter(twitter_user=current_user).all()
    for relationship in relationships:
        user_to_check = TwitterAccount.objects.filter(twitter_id=relationship.follows.twitter_id).first()
        if user_to_check and user_to_check.last_tweet_date:
            if user_to_check.last_tweet_date < date_to_compare_against:
                serializer = TwitterAccountSerializer(user_to_check)
                results.append(serializer.data)
    results.sort(key=sortKeyFunctionLastTweetDate)
    return Response(results)

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
@permission_classes([HasAPIKey])
def get_number_of_followers_whose_last_tweet_was_more_than_3_months_ago(request):
    body = json.loads(request.body)
    twitter_id_to_check = body['twitter_id']
    date_to_compare_against = utc.localize(datetime.now() - timedelta(days=90))
    results = []
    current_user = TwitterAccount.objects.filter(twitter_id=twitter_id_to_check).first()
    relationships = FollowingRelationship.objects.filter(twitter_user=current_user).all()
    for relationship in relationships:
        user_to_check = TwitterAccount.objects.filter(twitter_id=relationship.follows.twitter_id).first()
        if user_to_check and user_to_check.last_tweet_date:
            if user_to_check.last_tweet_date < date_to_compare_against:
                serializer = TwitterAccountSerializer(user_to_check)
                results.append(serializer.data)

    return Response(results)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
@permission_classes([HasAPIKey])
def unfollow_user(request):
    body = json.loads(request.body)
    token = body['token']
    logged_in_user_twitter_id = body['logged_in_user_id']
    twitter_id_to_unfollow = body['twitter_id']
    twitter_api = TwitterAPI()
    print(f"Unfollowing {twitter_id_to_unfollow}")
    twitter_api.unfollow_user(twitter_id_to_unfollow, token)
    currentUser = TwitterAccount.objects.filter(twitter_id=logged_in_user_twitter_id).first()
    userToUnfollow = TwitterAccount.objects.filter(twitter_id=twitter_id_to_unfollow).first()
    FollowingRelationship.objects.filter(twitter_user=currentUser, follows=userToUnfollow).delete()
    return Response({"success": True})