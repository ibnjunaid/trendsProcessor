from src import scrap_hashtag
from src.analyzer.main import predict_tweet, freqs, theta,label_tweet


def main(args):
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
                      'topic': 'hashtags', 'value': {"hashtags": ["#bengalururain"]}}]}

x = main(args)
prediction = predict_tweet(x['data'][0]['hashtag_details'], freqs=freqs, theta=theta)

print('----------------------------')

print('Prediction for', x['data'][0]['hashtag'], 'is ', label_tweet(prediction))