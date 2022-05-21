# def twitter_login(request):
#     twitter_api = TwitterAPI()
#     url, oauth_token, oauth_token_secret = twitter_api.twitter_login()
#     if url is None or url == '':
#         messages.add_message(request, messages.ERROR, 'Unable to login. Please try again.')
#         return render(request, 'authorization/error_page.html')
#     else:
#         twitter_auth_token = TwitterAuthToken.objects.filter(oauth_token=oauth_token).first()
#         if twitter_auth_token is None:
#             twitter_auth_token = TwitterAuthToken(oauth_token=oauth_token, oauth_token_secret=oauth_token_secret)
#             twitter_auth_token.save()
#         else:
#             twitter_auth_token.oauth_token_secret = oauth_token_secret
#             twitter_auth_token.save()
#         return redirect(url)
