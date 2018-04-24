from django.shortcuts import render,HttpResponse
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sentimental_analysis_app.utils.data_reader import read_csv_file, get_sentiment_intensity_analyzer

# Create your views here.
def profile(request):

	return HttpResponse(get_sentiment_intensity_analyzer(read_csv_file()))

def show_bar_chart(request):
	tweets = get_sentiment_intensity_analyzer(read_csv_file())
	bar_chart = tweets.sentiment_type.value_counts().plot(kind='bar',title="sentiment analysis")
	return HttpResponse("Showinng charts...")


