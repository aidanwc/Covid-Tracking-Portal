import re
import tweepy
import pandas as pd
from textblob import TextBlob
from datetime import datetime
from threading import Timer

x = datetime.today()
y = x.replace(day=x.day+1, hour=21, minute=41, second=0, microsecond=0)
delta_t = y-x
secs = delta_t.seconds+1

consumer_key = 'IXUhw2wnVqkcdbBTH0EAXNFib'
consumer_secret = '9qKsjBuOEfCzYFAh2FZn547IfQF8uz6vsqgckyaZcPYpCh6JWS'
access_token = '1209000765773295616-zJNYvN4MrQqsvMjMXOHXDDrMazAH6T'
access_token_secret = '0NqekKBM37Ol5cxuNdRF8apfAShUjf7q08PJ4PlrRyfp2'

hashtag_phrase = "Covid"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def sentiment_script():

        final = pd.DataFrame()

        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase + ' -filter:retweets', lang="en", tweet_mode='extended').items(80):

                text = tweet.full_text
                screen_name = tweet.user.screen_name

                text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

                blob = TextBlob(text)

                d = {'Tweet':[text], 'Username':[screen_name], 'Polarity':[blob.sentiment.polarity]}
                df = pd.DataFrame(data=d)

                final = final.append(df)

        print(final)
        print(final.mean())
        
#t = Timer(secs, sentiment_script())
#t.start()

sentiment_script()
