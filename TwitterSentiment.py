import tweepy 
from textblob import TextBlob
import pandas as pd

consumer_key = 'lO46pCFWbOtHtvzrnqzDbRnHx'
consumer_secret = 'eBy4N5qyWZMXxpUYmg2YZh85IMhRpMoXAq1gRu2HFf2xLROTEQ'

access_token = '1566998090418368512-e5hsZr1GN2MXr1JikVTtdyPjGvnM58'
access_token_secret = 'E4z34x7iCgFgtrPwX8XUtYrNQ9v1edMKbVqomycilh4vu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets("Jake Paul")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)           

columns = ['Time', 'User', 'Tweet']
data = []

for tweet in public_tweets:
    data.append(tweet.text)

df = pd.DataFrame(data, columns=columns)

print(df)

#to convert the file
df.to_csv('tweet.csv')
