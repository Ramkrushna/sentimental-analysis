from django.shortcuts import render,HttpResponse
import json
from django.shortcuts import redirect
from django.conf import settings
from sentimental_analysis_app.models import DemonitisationTweets
from sentimental_analysis_app.utils.data_writer import dump_csv_data_to_db
from django.db.models import Count
from django.core import serializers
from django.db import connection
from contextlib import closing

 
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/')

    return render(request,'home.html')

def process_data(request):
    print ("*****************Processing the CSV data**************************")
    # dump csv data to sqlite DB
    dump_csv_data_to_db()

    return HttpResponse(content="Successfully processed CSV data...!!!")

# Q1. Get percentage of different type of sentiment (Positive, Negative, Neutral)
def get_percentages_of_different_sentiments(request):
    chartData = []
    sql = "SELECT sentiment_type, count(*) as total FROM sentimental_analysis_app_demonitisationtweets GROUP BY sentiment_type;"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            chartData.append([row[0],row[1]])
    return HttpResponse(content=json.dumps({'chartData':chartData, 'chartTitle': "<center><h2>Percentage of Tweets Positive, Negative or Netural.</h2></center>"}), content_type="application/json")


# Q2. Get the most famous tweets
def get_most_famous_tweets(request):
    chartData = []
    sql = "SELECT x, screen_name, text, favorite_count FROM  sentimental_analysis_app_demonitisationtweets ORDER BY favorite_count DESC limit 10;"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            chartData.append({"id":row[0],"screenName":row[1],"text":row[2],"famousCount":row[3]})
    return HttpResponse(content=json.dumps({'chartData':chartData, 'chartTitle': "<center><h2>Showing Get the most famous tweets.</h2></center>"}), content_type="application/json")

# Q2. Get the most re-tweeted tweets
def get_most_re_tweeted_tweets(request):
    chartData = []
    sql = "SELECT x, screen_name, text, retweet_count FROM  sentimental_analysis_app_demonitisationtweets ORDER BY retweet_count DESC limit 10;"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            chartData.append({"id":row[0],"screenName":row[1],"text":row[2],"retweetCount":row[3]})
    return HttpResponse(content=json.dumps({'chartData':chartData, 'chartTitle': "<center><h2>Showing Get the most re-tweeted tweets.</h2></center>"}), content_type="application/json")


# Q4. Get percentage of different type of emotions (Joy, Sad, Fear etc.)
def get_percentages_of_different_emotions(request):
    chartData = []
    sql = "SELECT emotions, count(*) as total FROM sentimental_analysis_app_demonitisationtweets GROUP BY emotions ORDER BY emotions ASC;"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            chartData.append([row[0],row[1]])
    return HttpResponse(content=json.dumps({'chartData':chartData, 'chartTitle': "<center><h2>Showing Percentage Of Emotions (trust, disgust, surprise, sadness, joy, fear, anger)</h2></center>"}), content_type="application/json")


# Q5. Create Bar chart showing Tweet counts Device wise (twitter for Android, twitter Web client, Twitter for iPhone, Facebook, Twitter for iPad, etc.)
def get_tweet_counts_device_wise(request):
    chartData = []
    sql = "SELECT device_type, count(*) as total FROM sentimental_analysis_app_demonitisationtweets GROUP BY device_type ORDER BY total DESC;"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            chartData.append([row[0],row[1]])
    return HttpResponse(content=json.dumps({'chartData':chartData, 'chartTitle': "<center><h2>Showing Tweet counts Device wise (twitter for Android, twitter Web client etc.)</h2></center>"}), content_type="application/json")

def get_most_popular_users_chart_data(request):
    return HttpResponse(content=json.dumps({"Users":[
    	{"id": 11,
         "ScreenName": "Ram",
         "ReTweets": "123",
         "Tweets": "3"
    	  },
    	  {"id": 12,
         "ScreenName": "Rahul",
         "ReTweets": "122",
         "Tweets": "3"
    	  },
    	  {"id": 10,
         "ScreenName": "Ishar",
         "ReTweets": "120",
         "Tweets": "3"
    	  },

    	]}), content_type="application/json")


