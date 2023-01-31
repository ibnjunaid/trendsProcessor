from src import scrap_hashtag
from src.analyzer.predict import predict_hashtag_sentiment


def main(args):
    # print(type(args['messages'][0]['value']))
    #print("Scraper started")
    hashtags = args['messages'][0]['value']['hashtags']
    scraped_data = []
    if (hashtags == None):
        raise AssertionError("hashtag should be a list ")
    for hashtag in hashtags:
        hashtag_details = scrap_hashtag(trend_hashtag=hashtag)
        scraped_data.append({
            'hashtag': hashtag,
            'hashtag_details': hashtag_details
        })

    return {'data': scraped_data}

args = {'messages': [{'key': None, 'offset': 50, 'partition': 0,
                      'topic': 'hashtags', 'value': {"hashtags": ["#WWERaw"]}}]}

# x = main(args)
# print(x.get("data")[0].get("hashtag_details"))

# for k in x.get("data"):
#     print("Predecting for ", k.get("hashtag"))
#     y_hat = m.predict_tweet(k.get("hashtag_details"), m.freqs, m.theta)
#     print(y_hat)
#     if y_hat > 0.5:
#         print('Positive sentiment')
#     elif y_hat==0.5:
#         print('Neutral sentiment')
#     else: 
#         ('Negative sentiment')

y_hat = predict_hashtag_sentiment('I am feeling good')
print(y_hat)
if y_hat > 0.5:
    print('Positive sentiment')
elif y_hat==0.5:
    print('Neutral sentiment')
else: 
    print('Negative sentiment')