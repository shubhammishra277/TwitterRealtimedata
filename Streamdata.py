import tweepy
import os
import time 

from confluent_kafka import Producer
import optparse
from loggermodule import logger_test
from configgetter import configparser

import sys
reload(sys)

sys.setdefaultencoding('utf8')


class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api, filepath):
        self.filepath=filepath
        self.api=api
        super(tweepy.StreamListener,self).__init__()

    def on_status(self, status):
        logger_test.debug("inside on_status method")
        f=open("%s"%self.filepath,"a+")
        logger_test.debug("all Tweets :%s"%status.text)
        k=[i for i in str(status.text).encode("utf-8").split(" ") if i.startswith("#")]
        if len(k)!=0:
            logger_test.info("Tweets with hashtags :%s"%status.text)
            f.write("tweet:%s\n"%str(status.text).encode("utf-8"))
            for i in k: 
                f.write("Hastagused:%s\n"%i)
                
        return True
    def on_error(self, status_code):
        if status_code == 420:
            return False


class twitter_data_push(MyStreamListener):
    
    def __init__(self,client_name,searchstring,filepath):
        
        t1=configparser()
        platformname="twitter"
        self.filepath=filepath
        self.searchstring=searchstring.split(",")
        client_name,consumer_key,consumer_secret,access_token_key,access_token_secret=t1.configparse(client_name, platformname)
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token_key, access_token_secret)
        try:
          self.api = tweepy.API(self.auth)
    
          logger_test.info("succesful authentication with twitter")
        except Exception,e:
            logger_test.exception("error occured while doing authentication with twitter with following error:%s"%str(e))
            sys.exit("authentication failed")
            
    def get_data(self):
        
        logger_test.debug("inside get_data function")
        myStream = tweepy.Stream(self.auth, listener=MyStreamListener(self.api,self.filepath))
        logger_test.info("self.searchstring %s"%self.searchstring)
        myStream.filter(track=self.searchstring,async=True)
        
if __name__=="__main__":
    parser = optparse.OptionParser(description='Optional app description')
    parser.add_option('-u','--username', 
                    help='enter the username for which you have access token,consumer_token etc.')
    parser.add_option('-s','--search_string',
                    help='Query string which you want to filter for realtimedata',
                    default="Narendra Modi")
    parser.add_option('-f','--filepath', 
                    help='enter the filepath in which you want to write real time data ')
    
    try:
      options, args = parser.parse_args()
    except Exception,e:
        logger_test.exception("Sys arguements parsing failed with following errors:%s"%str(e))
    logger_test.info("arguemts parsed from command line are:%s "%options)
    
    os.system("rm %s"%options.filepath)
    t1=twitter_data_push(str.lower(options.username),options.search_string,options.filepath)
    t1.get_data()
    
        
        
        
        
        
        
        
        
