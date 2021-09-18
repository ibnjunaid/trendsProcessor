from datetime import date
import twint
import pymongo
import db.py_mongo as py_mongo

#This function scrapes a batch of 200 tweets for the given trend

def retrive_tweets(trend, limit = 100, isVerified = True):
    config = twint.Config()
    config.Search = trend
    config.Verified = isVerified
    config.Min_likes = 100
    config.Lang = 'en'
    config.Count = True
    config.Limit = limit
    config.Store_object = True
    # Initiate the search
    twint.run.Search(config)
    # Return tweets
    return twint.output.tweets_list
#end of fn

def save_to_db(tweets):
    py_mongo.save_to_collection(collection_name='tweets', tweets = tweets)


















if __name__ == '__main__':
    retrive_tweets('#PAKvNZ')