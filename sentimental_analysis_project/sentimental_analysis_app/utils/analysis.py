import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
import seaborn as sns


# Q1. What percentage of tweets is negative, positive or neutral?
def get_analized_sentiments(data):
    '''
    Utility function to classify the polarity of all the tweets using textblob.

    '''
    counter = {}

    sid = SentimentIntensityAnalyzer()

    data['sentiment_compound_polarity']=data.text.apply(lambda x:sid.polarity_scores(x)['compound'])
    data['sentiment_neutral']=data.text.apply(lambda x:sid.polarity_scores(x)['neu'])
    data['sentiment_negative']=data.text.apply(lambda x:sid.polarity_scores(x)['neg'])
    data['sentiment_pos']=data.text.apply(lambda x:sid.polarity_scores(x)['pos'])

    data['sentiment_type']=''
    data.loc[data.sentiment_compound_polarity>0,'sentiment_type']='POSITIVE'
    data.loc[data.sentiment_compound_polarity==0,'sentiment_type']='NEUTRAL'
    data.loc[data.sentiment_compound_polarity<0,'sentiment_type']='NEGATIVE'

    return data

#Q2. a. Get the most famous tweeted tweets
def get_most_famous_tweets(data):
	'''
    Utility function to classify the polarity of all the tweets using textblob.

    '''
    return data.iloc[data['favoriteCount'].argmax()]['text'])


#Q2. b. Get the most famous re-tweeted tweets
def get_most_famous_retweets(data):
	'''
    Utility function to classify the polarity of all the tweets using textblob.

    '''
    return data.iloc[data['retweetCount'].argmax()]['text'])


#Q3. The number of retweet per hour
def get_retweets_per_hour_count():
    data['hour'] = pd.DatetimeIndex(data['created']).hour
    tweets_hour = data.groupby(['hour'])['retweetCount'].sum()
    data['text_len'] = data['text'].str.len()
    tweets_all_hour = data.groupby(['hour'])['text_len'].sum()


tweets_hour.transpose().plot(kind='line',figsize=(6.5, 4))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('The number of retweet per hour', bbox={'facecolor':'0.8', 'pad':0})

