from datetime import date
import twint

#This function scrapes a batch of 200 tweets for the given trend

def retrive_tweets(trend, limit = 50, isVerified = False):
    config = twint.Config()
    config.Search = trend
    config.Verified = isVerified
    config.Min_likes = 100
    # config.Lang = 'en'
    # config.Count = True
    config.Limit = limit
    config.Store_object = True
    config.Filter_retweets = True
    config.Hide_output = True
    config.Country = "India"
    # config.Images = True
    # config.Videos = True
    # config.Since = str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day -1)
    # Initiate the search
    twint.run.Search(config)
    return twint.output.tweets_list
#end of fn














if __name__ == '__main__':
    retrive_tweets('#RakshaBandhan')