# Twitter Stuff

Messing with the Twitter API using Python and Tweepy

## Stuff it does

This allows you to pull information about a Twitter account, given its screen name (@).
For now, the code fetches these:
* Account information:
  * Name (as displayed on the profile)
  * Screen Name (@)
  * Bio
  * Location
  * Following count
  * Followers count
  * Tweets count
  * Favourites count
  * Account creation date
  * Account time zone (if set)
  * Account verification (accounts with the tick next to the name)
* Last tweet information (if available):
  * Last tweet made
  * Date
  * Retweets
  * Favourites

## Requirements

* Python 3.5.2
* Tweepy 3.6.0
