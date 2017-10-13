import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'TAokzoXhKtEkfLE6vDAWC6x1J'
consumer_secret = 'qJdIYVDr616FyfCn9ouyGUpCj0WYYYaASe9ogCYi39WmDhUMV8'
access_token = '3980764872-mb2xFrRK2Y84pN7NuNtmuu8dz5tBX9oz6jJ0nrx'
access_token_secret = '7miDRxtmw9CJ36OANwqJYjKHBuPTH2I3PliOOkZddo9c4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ub.csv', 'a', encoding='utf-8')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#newton",count=50,
                           lang="en").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
