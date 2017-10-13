#import regex
import re
import csv
#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    #removing emoticon
    emoji_pattern = r'/[U0001F601-U0001F64F]/u'
    hi = re.sub(emoji_pattern, '', 'hello')
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it
fp = open('ub.csv', 'r')
line = fp.readline()
processed = open('file2.csv','a',encoding ='utf-8');
csvWriter = csv.writer(processed)

while line:
    processedTweet = processTweet(line)
    print (processedTweet)
    csvWriter.writerow([ processedTweet.encode('utf-8')])
    line = fp.readline()
#end loop
fp.close()
