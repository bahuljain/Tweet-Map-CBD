# -*- coding: utf-8 -*-

from pymongo import Connection

if __name__ == "__main__":
    con = Connection()
    
    
    #if there is a database available with that name then it accesses it
    #if there isnt a database with the given name then it simply creates a new database    
    db = con.twitterDatabase_test
    
    # again a collection is accessed, if it doesnt exist then a collection with this name is created
    tweetsCollection = db.tweetsCollection_test
    
#    tweetsCollection.insert({'id':'1234','text':'Hello','location':'USA'})
#    tweetsCollection.insert({'id':'1235','text':'Hello :)','location':'India'})
#    tweetsCollection.insert({'id':'1236','text':'Hello :(','location':'UK'})
    
    tweets = tweetsCollection.find()
    size = tweetsCollection.count()
    print 'FIND'
    print 'Number of Rows ' + `size`
    count = 0;
    for tweet in tweets:
        if len(tweet['category'])==0:
            count = count +1
            print tweet['text']
    print count
#    coordinates = []
#    for tweet in tweets:
##            print tweet['text']
#            coordinates.append({'lat':tweet['coordinates'][0],'long':tweet['coordinates'][1]})
##            print tweet['category']
#    data = {'coordinates':coordinates}
#    print coordinates           
#    
#    tweets = tweetsCollection.find({'location':'India'})
#    
#    print 'FIND INDIAN Tweets'
#    
#    for tweet in tweets:
#            print tweet
#    
    
#    tweets = tweetsCollection.find_one({'location':'India'})
#    tweets['text'] = 'Hello I am Bahul Jain :)'
#    tweetsCollection.save(tweets)
#
#    for tweet in tweetsCollection.find({'location':'India'}):
#        print tweet
    
     # remove all shit
#    for tweet in tweetsCollection.find():
#        tweetsCollection.remove(tweet)
#       