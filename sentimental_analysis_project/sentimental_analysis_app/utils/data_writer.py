from sentimental_analysis_app.models import DemonitisationTweets
from sentimental_analysis_app.utils.analysis import get_analized_sentiments
import os
import csv
from datetime import datetime
from django.db import connection
from contextlib import closing
from django.db import connection
from django.utils import timezone



def set_analyzed_sentiment_type_to_data_set(data_set):
     analyzed_data = get_analized_sentiments()
     for ds in data_set:
     	if int(ds['X']) in analyzed_data['sentiment_type']:
         	ds['sentiment_type'] = analyzed_data['sentiment_type'].get(int(ds['X']))
     return data_set


def clean_existing_table_data():
     sql = "DELETE FROM sentimental_analysis_app_demonitisationtweets;"
     with closing(connection.cursor()) as cursor:
        cursor.execute(sql)

def sql_batch_insert(data_set):
    sql = 'INSERT INTO sentimental_analysis_app_demonitisationtweets (x,tweet_id,text,favorited,favorite_count,reply_to_sn,created,truncated,reply_to_sid,reply_to_uid,status_source,screen_name,retweet_count,is_retweet,retweeted,sentiment_type) VALUES {}'

    params = []
   
    for tweet in data_set:
        try:
            values = '({X},{id},"{text}",{favorited},{favorite_count},"{reply_to_sn}","{created}",{truncated},"{reply_to_sid}","{reply_to_uid}","{status_source}","{screen_name}","{retweet_count}",{is_retweet},{retweeted},"{sentiment_type}")'.format(X=tweet['X'], id=tweet['id'],
        	                                              text=tweet['text'].replace('"',"'"),favorited=tweet['favorited'],
        	                                              favorite_count=tweet['favoriteCount'],
        												  reply_to_sn=tweet['replyToSN'],
        												  created=tweet['created'],
        												  truncated=tweet['truncated'],
        												  reply_to_sid=tweet['replyToSID'],
        												  reply_to_uid=tweet['replyToUID'],
        												  status_source=tweet['statusSource'].replace('"',"'"),
        												  screen_name=tweet['screenName'].replace('"',"'"),
        												  retweet_count=tweet['retweetCount'],
        												  is_retweet=tweet['isRetweet'],
        												  retweeted=tweet['retweeted'],
        												  sentiment_type = tweet['sentiment_type']
        												  ) 
            params.append(values)
        except Exception as err:
            pass
    with closing(connection.cursor()) as cursor:
        values_section = ",".join(params)
        sql = sql.format(values_section)
        cursor.execute(sql)



# def convert_date_to_django_format(date_str):
#     format = '%d/%m/%y %H:%M'
#     d = datetime.strptime(date_str, format)
#     formated_date = d.strftime("%Y-%m-%d %H:%M:%S")
#     return formated_date

def dump_csv_data_to_db():
    """
    """
    file_path = os.path.dirname((__file__))+"/../input_data/demonetization-tweets.csv"	
    data = csv.DictReader(open(file_path))
    print ("loading csv to mysql")
    tweets = list(data)
    set_analyzed_sentiment_type_to_data_set(tweets)
    clean_existing_table_data()
    sql_batch_insert(tweets)
    print ("Dumped csv data to mysql successfully...")

