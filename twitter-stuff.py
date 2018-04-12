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
	try:
		user = api.get_user(sn)
		print('Name: ' + user.name)
		print('Screen Name: ' + user.screen_name)
		print('Bio: ' + user.description)
		if not user.location:
			print('Location: Unknown')
		else:
			print('Location: ' + user.location)
		print('Friends: ' + str(user.friends_count))
		print('Followers: ' + str(user.followers_count))
		print('Tweets: ' + str(user.statuses_count))
		print('Favourites: ' + str(user.favourites_count))
		print('Creation Date: ' + str(user.created_at))
		if not user.time_zone:
			print("Time Zone: Unknown")
		else:
			print('Time Zone: ' + user.time_zone)
		if user.verified:
			print("This account is verified.")
		print('===============================================')
		if user.protected:
			print("This account's tweets are protected, and therefore cannot be viewed.")
		else:
			try:
				print('Last tweet: ' + user.status.text)
				print('Last tweet date: ' + str(user.status.created_at))
				print('Retweets: ' + str(user.status.retweet_count))
				print('Favourites: ' + str(user.status.favorite_count))
			except:
				print("This account has not tweeted anything yet.")
	except:
		print("This account does not exist or has been suspended.")
pass

sn = ''
while not sn:
	sn = input('Please enter a screen name: ')
me(sn)
