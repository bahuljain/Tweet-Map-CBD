# -*- coding: utf-8 -*-
import json
#import pandas as pd
#import matplotlib.pyplot as plt

class TwitterDataHandle:
    'Handles bunch of tweets passed in JSON format'
    
    def __init__(self, tweetsData):
        self.tweetsList = []
        for tweet in tweetsData:
            self.tweetsList.append(Tweet(tweet))
    
    def getTweet(self, tweetIndex):
        return self.tweetsList[tweetIndex]
		
    def getInnerTweetsBy(self, key, innerKey):
        return map(lambda tweet:tweet.getValueByInnerKey(key, innerKey), self.tweetsList)	
        
    def getTweetsBY(self, key):
        return map(lambda tweet:tweet.getValueByKey(key), self.tweetsList)
    
class Tweet:
    'Handles a tweet passed in JSON format'
    
    def __init__(self, tweet):
        self.tweet = tweet
    
    def getValueByKey(self, key):
        return self.tweet[key]
		
    def getValueByInnerKey(self, key, innerKey):
		if self.tweet[key] != None:
			return self.tweet[key][innerKey]
		else:
			return None

tweetsDataPath = 'twitterSet.txt'

tweetsData = []
tweetsFile = open(tweetsDataPath, "r")
for line in tweetsFile:
    try:
        tweet = json.loads(line)
        tweetsData.append(tweet)
    except:
        continue

print len(tweetsData)

#for i in range(1,100):
	#if tweetsData[i]['geo'] != None:
	#	print tweetsData[i]['geo']['coordinates']
	
twitterHandler = TwitterDataHandle(tweetsData)
#tweet = twitterHandler.getTweet(0)
#print tweet.getText().encode('ascii','ignore').decode('ascii')

#print tweetsData[0]['text'].encode('ascii','ignore').decode('ascii')
 
tweets = {'text':[],'lang':[],'place':[]}
tweets['text'] = twitterHandler.getTweetsBY('text')   
tweets['lang'] = twitterHandler.getTweetsBY('lang')   
tweets['place'] = twitterHandler.getInnerTweetsBy('geo','coordinates')
for place in tweets['place']:
    if place != None:
        placehandle = open('tweetplace.txt', 'a')
        placehandle.writelines(str(place[0])+" "+str(place[1]))
        placehandle.close()

#print tweets

