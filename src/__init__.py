import src.scraper.get_trends as scraper
import src.preprocessor.pre as preprocessor
import functools

def scrap_hashtag(trend_hashtag):
    tweet_object_list = scraper.retrive_tweets(trend_hashtag)
    tweet_content_list: list[str] = map(lambda a: a.tweet, tweet_object_list)
    aggregated_tweet = functools.reduce(reducer, tweet_content_list)
    return aggregated_tweet


def reducer(tweet_a,tweet_b) -> str:
    return tweet_a + tweet_b