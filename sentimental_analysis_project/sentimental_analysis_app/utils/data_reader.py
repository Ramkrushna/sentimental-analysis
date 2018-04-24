
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *

from nltk import tokenize
import numpy as np
import pandas as pd
import logging
import os

# Get an instance of a logger
logger = logging.getLogger(__name__)


def read_csv_file():
	try:
		file_path = os.path.dirname((__file__))+"/../input_data/demonetization-tweets.csv"
		tweets=pd.read_csv(file_path,encoding = "ISO-8859-1")
		return tweets
	except Exception as error:
		logger.error("Error occurred while reading input file: {}".format(error))


def get_sentiment_intensity_analyzer(tweets):
	sid = SentimentIntensityAnalyzer()

	tweets['sentiment_compound_polarity']=tweets.text.apply(lambda x:sid.polarity_scores(x)['compound'])
	tweets['sentiment_neutral']=tweets.text.apply(lambda x:sid.polarity_scores(x)['neu'])
	tweets['sentiment_negative']=tweets.text.apply(lambda x:sid.polarity_scores(x)['neg'])
	tweets['sentiment_pos']=tweets.text.apply(lambda x:sid.polarity_scores(x)['pos'])
	tweets['sentiment_type']=''
	tweets.loc[tweets.sentiment_compound_polarity>0,'sentiment_type']='POSITIVE'
	tweets.loc[tweets.sentiment_compound_polarity==0,'sentiment_type']='NEUTRAL'
	tweets.loc[tweets.sentiment_compound_polarity<0,'sentiment_type']='NEGATIVE'
	return tweets.head()

def get_bar_chart_data(tweets):
	return tweets.sentiment_type.value_counts().plot(kind='bar',title="sentiment analysis")