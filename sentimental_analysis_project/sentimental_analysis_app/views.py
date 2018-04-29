from django.shortcuts import render,HttpResponse
import json
#import numpy as np # linear algebra
#import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#from sentimental_analysis_app.utils.data_reader import read_csv_file, get_sentiment_intensity_analyzer
from django.shortcuts import redirect
from django.conf import settings


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    #return HttpResponse("Welcome {}".format(request.user.username))
    return render(request,'profile.html')
    #return HttpResponse(get_sentiment_intensity_analyzer(read_csv_file()))

def get_percentages_of_different_sentiments(request):
    chartData = [
                        ['Neutral', 10],
                        ['Negative', 30],
                        ['Positive', 60],
                    ]
    return HttpResponse(content=json.dumps(chartData), content_type="application/json")
def show_bar_chart(request):
    test_list_dict = [{"label": "Recommended", "value": 60}, {"label": " You", "value": 50}, {"label": "Peers", "value": 40 }]

    return HttpResponse(content=json.dumps(test_list_dict), content_type="application/json")


