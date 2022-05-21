from rest_framework import serializers
from .models import TwitterAccount, FollowingRelationship

class TwitterAccountSerializer(serializers.Serializer):
    twitter_id = serializers.CharField(max_length=512)
    twitter_username = serializers.CharField(max_length=255)
    twitter_name = serializers.CharField(max_length=255)
    last_tweet_date = serializers.DateTimeField()

    # main = serializers.PrimaryKeyRelatedField(many=True, queryset=FollowingRelationship.objects.all())
    # follows = serializers.PrimaryKeyRelatedField(many=True, queryset=FollowingRelationship.objects.all())
    # class Meta:
    #     model = TwitterAccount
    #     fields = ('pk', 'twitter_id', 'twitter_username', 'last_tweet_date')

class FollowingRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowingRelationship
        fields = ('twitter_user', 'follows')
