import tweepy
from datetime import datetime, timedelta

from config import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
	)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def me(sn):
	user = api.get_user(sn)
	print('Name: ' + user.name)
	print('Screen Name: ' + user.screen_name)
	if not user.location:
		print('Location: Unknown')
	else:
		print('Location: ' + user.location)
	print('Friends: ' + str(user.friends_count))
	print('Followers: ' + str(user.followers_count))
	print('Tweets: ' + str(user.statuses_count))
	print('Favourites: ' + str(user.favourites_count))
	print('Creation Date: ' + str(user.created_at))
	print('===============================================')
	print('Last tweet: ' + user.status.text)
	print('Last tweet date: ' + str(user.status.created_at))
	print('Retweets: ' + str(user.status.retweet_count))
	print('Favourites: ' + str(user.status.favorite_count))
pass

sn = ''
while not sn:
	sn = input('Please enter a screen name: ')
me(sn)
