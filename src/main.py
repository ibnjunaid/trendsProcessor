import scraper.get_trends as scraper
import preprocessor.pre as preprocessor

tweets = scraper.retrive_tweets("#earthquake")

top_urls = preprocessor.extract_top_urls(tweets)
top_mentions = preprocessor.extract_top_mentions(tweets)
top_hashtags = preprocessor.extract_top_hashtags(tweets)

print(top_hashtags)
#scraper.save_to_db(tweets)
