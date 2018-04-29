from django.db import models

# Create your models here.

# class DemonitisationTweets(models.Model):
#     x = models.IntegerField()
#     tweet_id = models.CharField(max_length=30)
#     text = models.CharField(max_length=700)
#     favorited = models.BooleanField()
#     favorite_count = models.IntegerField() # likes
#     reply_to_sn = models.CharField(max_length=30)
#     created = models.DateTimeField(max_length=30)# TODO use date time with DD-MM-YYYY hh:mm
#     truncated = models.BooleanField()
#     reply_to_sid = models.CharField(max_length=30)
#     reply_to_uid = models.CharField(max_length=30)
#     status_source = models.CharField(max_length=150)
#     screen_name = models.CharField(max_length=30)
#     retweet_count = models.IntegerField()
#     is_retweet = models.BooleanField()
#     retweeted = models.BooleanField()
#     # Newly added columns
#     sentiment_compound_polarity = models.FloatField(max_length=30, null=True) # it should support 4 decimal places
#     sentiment_neutral = models.FloatField(max_length=30, null=True) # it should support 4 decimal places
#     sentiment_negative = models.FloatField(max_length=30, null=True) # it should support 4 decimal places
#     sentiment_pos = models.FloatField(max_length=30, null=True) # it should support 4 decimal places
#     sentiment_type = models.CharField(max_length=20, null=True)
#     date = models.DateField(max_length=30, null=True)
#     hour = models.IntegerField(null=True)
#     minute = models.IntegerField(null=True)
#     emotions = models.CharField(max_length=30, null=True)
#     device_type = models.CharField(max_length=30, null=True)



class DemonitisationTweets(models.Model):
    x = models.CharField(max_length=30)
    tweet_id = models.CharField(max_length=30,null=True)
    text = models.CharField(max_length=700,null=True)
    favorited = models.CharField(max_length=30,null=True)
    favorite_count = models.CharField(max_length=30,null=True) # likes
    reply_to_sn = models.CharField(max_length=30,null=True)
    created = models.CharField(max_length=30,null=True)# TODO use date time with DD-MM-YYYY hh:mm
    truncated = models.CharField(max_length=30,null=True)
    reply_to_sid = models.CharField(max_length=30,null=True)
    reply_to_uid = models.CharField(max_length=30,null=True)
    status_source = models.CharField(max_length=150,null=True)
    screen_name = models.CharField(max_length=30,null=True)
    retweet_count = models.CharField(max_length=30,null=True)
    is_retweet = models.CharField(max_length=30,null=True)
    retweeted = models.CharField(max_length=30,null=True)
    # Newly added columns
    sentiment_compound_polarity = models.CharField(max_length=30, null=True) # it should support 4 decimal places
    sentiment_neutral = models.CharField(max_length=30, null=True) # it should support 4 decimal places
    sentiment_negative = models.CharField(max_length=30, null=True) # it should support 4 decimal places
    sentiment_pos = models.CharField(max_length=30, null=True) # it should support 4 decimal places
    sentiment_type = models.CharField(max_length=20, null=True)
    date = models.CharField(max_length=30, null=True)
    hour = models.CharField(null=True,max_length=30)
    minute = models.CharField(null=True,max_length=30)
    emotions = models.CharField(max_length=30, null=True)
    device_type = models.CharField(max_length=30, null=True)

class Tweets(models.Model):
    X = models.IntegerField()
    text = models.CharField(max_length=700)
    favorited = models.BooleanField()
    favoriteCount = models.IntegerField() # likes
    replyToSN = models.CharField(max_length=30)
    created = models.DateTimeField(max_length=30)# TODO use date time with DD-MM-YYYY hh:mm
    truncated = models.BooleanField()
    replyToSID = models.CharField(max_length=30)
    id = models.CharField(primary_key=True, max_length=30)
    replyToUID = models.CharField(max_length=30)
    statusSource = models.CharField(max_length=150)
    screenName = models.CharField(max_length=30)
    retweetCount = models.IntegerField()
    isRetweet = models.BooleanField()
    retweeted = models.BooleanField()
