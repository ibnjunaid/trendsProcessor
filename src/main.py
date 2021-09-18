import scraper.get_trends as scraper

tweets = scraper.retrive_tweets("#earthquake")
scraper.save_to_db(tweets)
