import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
consumer_key = "SaXgDexQIkKEM40CNXISFJaPx"
consumer_secret = "6oFycseVmK9IHp85ST8lYKFaUTevIExZYQXS42sooXMT4ZQMmo"
access_token = "3030140488-n5IQ7bIVV8yr3cyOF1c7uQWjpYP4vYMnWENzSp3"
access_token_secret = "CthbkgmtrxkenYyVPbV6ihBA1niNE2LkO9VRGx6lI6Id6"
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)


class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            with open('tweetcollects.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'stock market'
    stream.filter(track=['emotions','netflix','avengers','usopen','happy','bahubali','marvel','wonderwoman','pmoindia','petrol','kansascity',
                         'umkc','jonsnow','khaleesi','emmys','ellen','logan','wolverine','hobbit','bigboss','telugu','narcos',
                         'flash','arrow','vampiredairies','incredibles','the','subtle','art','of','not','giving','a'])