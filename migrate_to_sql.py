import json
import pymongo
import tweepy
import psycopg2
import sys
from datetime import tzinfo, timedelta, datetime


conn = psycopg2.connect("dbname=TwDatabase user=postgres host=localhost password=postgres")
cur = conn.cursor()
#counter = 0

count = 0
db = pymongo.MongoClient().carga_icc1002
collection = db.icccualquiercosa
tweets = collection.find()

for tweet in tweets:
	print count
	count += 1
	place = ""

	try:
		place = tweet['place']
	except:
		print "place error"
	text = " "
        tweetId = str(tweet['_id'])
        created = tweet['created_at']
	inReplyToStatusId = ""
	inReplyToYuserId = ""
	try:
        	inReplyToStatusId = tweet['in_reply_to_status_id']
        	inReplyToYuserId = tweet['in_reply_to_user_id']
	except:
		print "error"
	user = ""
	try:
        	user = tweet['user']
	except:
		print "user error"
	userId = ""
	userDescription = ""
	userFollowers = ""
	userLocation = ""
	userFriends = ""
	userTimeZone = ""
	if user != "":
        	userId = user['id']
        	userDescription = user['description']
        	userFollowers = user['followers_count']
        	userLocation = user['location']
        	userFriends = user['friends_count']
        	userTimeZone = user['time_zone']

	try:
		text = tweet['text']
	except:
		print " text error"
	try:	
		cur.execute("INSERT INTO carga(twitt_id, created, twitt_text, time_zone,twitt_location,reply_id,reply_user_id, user_id,user_description,followers_count,friends_count,place) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (tweetId, created, text, userTimeZone,userLocation,inReplyToStatusId,inReplyToYuserId, userId,userDescription, userFollowers, userFriends, place))
		conn.commit()
	except:
		print "BIG ERROR"
      
cur.close()
conn.close()


	
print "FINISH"

