# -*- coding: utf-8 -*-

from pymongo import Connection

if __name__ == "__main__":
    con = Connection()
    
    
    #if there is a database available with that name then it accesses it
    #if there isnt a database with the given name then it simply creates a new database    
    db = con.twitterDatabase_test
    
    # again a collection is accessed, if it doesnt exist then a collection with this name is created
    tweetsCollection = db.tweetsCollection_test
    for tweet in tweetsCollection.find():
        tweetsCollection.remove(tweet)
    