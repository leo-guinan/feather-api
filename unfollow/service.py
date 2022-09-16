from datetime import datetime, timedelta

from pytz import utc
from tweepy import TooManyRequests

from client.models import StaffAccount
from twitter.service import get_most_recent_tweet
from unfollow.models import AccountCheck


def get_twitter_account_info_for_check(account_check_id):
    check = AccountCheck.objects.filter(id=account_check_id).first()
    print(f'checking account_check: {account_check_id}')
    if account_recently_checked(check):
        print("account recently checked.")
        return

    twitter_account = check.account
    if account_tweeted_recently(twitter_account):
        print("account tweeted recently.")
        check.last_analyzed = utc.localize(datetime.now())
        check.save()
        return

    for client_account in check.requests.all():
        try:
            print(f"running check for client account: {client_account.id}")
            get_most_recent_tweet(client_account_id=client_account.id,
                                  twitter_id_to_lookup=twitter_account.twitter_id)
            check.last_analyzed = utc.localize(datetime.now())
            check.save()
            return
        except TooManyRequests:
            # do nothing, rate limit issues. Try next client_account
            continue
    # if made it here, tried all client accounts already, so let's try the staff accounts
    staff = StaffAccount.objects.filter(client__name="UNFOLLOW").all()
    for staff_members in staff:
        try:
            print(f'running staff check with id: {staff_members.id}')
            get_most_recent_tweet(client_account_id=staff_members.id,
                                  twitter_id_to_lookup=twitter_account.twitter_id,
                                  staff_account=True)
            check.last_analyzed = utc.localize(datetime.now())
            check.save()
            return
        except TooManyRequests:
            # do nothing, probably rate limit issues. Try next staff_member
            continue


def account_recently_checked(check):
    return check.last_analyzed and check.last_analyzed > (
        utc.localize(datetime.now() - timedelta(days=30)))


def account_tweeted_recently(twitter_account):
    return twitter_account.last_tweet_date and twitter_account.last_tweet_date > (
        utc.localize(datetime.now() - timedelta(days=90)))
