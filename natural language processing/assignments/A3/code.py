import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import json
import re
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener 
import os
#os.chdir('F:/SEM 05/NATURAL LANGUAGE PROCESSING/ASSIGNMENTS/Assignment 3')

consumer_key = "UQ8XFSgXLOSnpm8FLt2ggi0c4"
consumer_secret = "9suCc5INoh69KRflUER83K2kAINYXTkT2gm2jO8LttPKENVJ4M"
access_token = "1111498145177849856-P64xYnQ7LMata8ULOHeMRSmngqsaKA"
access_secret= "ICWLB2vC4CIMrNaGgx6BqbJHqJX2RSCFdAwcCYsxYR4sr"



auth= OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)


file= open('flood_raw.dat','a')


class Mylistener(StreamListener):
    def _init_(self, api=None):
        super(StreamListener,self)._init_()
        self.num_tweet = 0
        
    def on_data(self,data):
        try:
            with open('flood_filtered.dat','a') as f:
                tweet=json.loads(data)
                
                if tweet ['lang']=="en":
                    file.write(data)
                    file.write('\n')
                  
                if tweet['lang']=='en' :
                    if self.num_tweet<2000:
                        print(json.dumps(tweet["text"],indent=4))
                        f.write(tweet["text"])
                        f.write("\n")
                        self.num_tweets += 1
                        
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True    
                    
def on_error(self,status):
        print(status)
        return True
def on_status(self,status):
    if status.retweeted_status=='true':
        return
    print(status)
      
mytwitter_stream = Stream(auth,Mylistener())
mytwitter_stream.filter(track=['#banjir', '#flood', '#FloodRelief','#FloodMalaysia','#FloodSelangor'])
file.close()
print("done")