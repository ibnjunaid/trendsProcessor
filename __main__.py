from src import scrap_hashtag


def main(args):
    # print(type(args['messages'][0]['value']))
    print("Scraper started")
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
                      'topic': 'hashtags', 'value': {"hashtags": ["#Pathaan500CroreEvent"]}}]}

print(main(args))
