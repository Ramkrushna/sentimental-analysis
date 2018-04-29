
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *

from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import numpy as np
import pandas as pd
import logging
import os
import re

# Get an instance of a logger
logger = logging.getLogger(__name__)

def clean(text):
    lettersOnly = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(text))
    tokens = word_tokenize(lettersOnly.lower())
    stops = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stops]
    tokensPOS = pos_tag(tokens)
    tokensLemmatized = []
    for w in tokensPOS:
        tokensLemmatized.append(WordNetLemmatizer().lemmatize(w[0]))
    clean = " ".join(tokensLemmatized)
    return clean

def read_csv_file():
	try:
		logger.info("Reading demonetization-tweets file...")
		file_path = os.path.dirname((__file__))+"/../input_data/demonetization-tweets.csv"
		tweets = pd.read_csv(file_path,encoding = "ISO-8859-1")
		return tweets
	except Exception as error:
		logger.error("Error occurred while reading input file: {}".format(error))

