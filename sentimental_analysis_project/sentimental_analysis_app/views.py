from django.shortcuts import render,HttpResponse
import json
from django.shortcuts import redirect
from django.conf import settings
from sentimental_analysis_app.models import DemonitisationTweets
from sentimental_analysis_app.utils.data_writer import dump_csv_data_to_sqlite_db
from sentimental_analysis_app.utils.data_writer import dump_csv_data_to_sqlite_db
from django.db.models import Count
from django.core import serializers
from django.db import connection
from contextlib import closing

 
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/')

    return render(request,'profile.html')

def process_data(request):
    print ("*****************Processing the CSV data**************************")
    # dump csv data to sqlite DB
    dump_csv_data_to_sqlite_db()

    return HttpResponse(content=json.dumps({"message": "Success"}), content_type="application/json")

# Q1. Get percentage of different type of sentiment (Positive, Negative, Neutral)
def get_percentages_of_different_sentiments(request):
    chartData = []
    sql = "SELECT sentiment_type, count(*) as total FROM sentimental_analysis_app_demonitisationtweets GROUP BY sentiment_type;"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            chartData.append([row[0],row[1]])
    return HttpResponse(content=json.dumps(chartData), content_type="application/json")


def get_most_popular_users_chart_data(request):
    print ("********************IN")
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


