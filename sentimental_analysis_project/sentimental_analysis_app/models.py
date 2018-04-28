from django.db import models

# Create your models here.

class DemonitisationTweets(models.Model):
    tweet_id = models.CharField(max_length=30)
    text = models.CharField(max_length=700)
    favorited = models.BooleanField()
    favorite_count = models.IntegerField() # likes
    reply_to_sn = models.CharField(max_length=30)
    created = models.DateTimeField(max_length=30)# TODO use date time with DD-MM-YYYY hh:mm
    truncated = models.BooleanField()
    reply_to_sid = models.CharField(max_length=30)
    reply_to_uid = models.CharField(max_length=30)
    status_source = models.CharField(max_length=150)
    screen_name = models.CharField(max_length=30)
    retweet_count = models.IntegerField()
    is_retweet = models.BooleanField()
    retweeted = models.BooleanField()
    # Newly added columns
    sentiment_compound_polarity = models.FloatField(max_length=30) # it should support 4 decimal places
    sentiment_neutral = models.FloatField(max_length=30) # it should support 4 decimal places
    sentiment_negative = models.FloatField(max_length=30) # it should support 4 decimal places
    sentiment_pos = models.FloatField(max_length=30) # it should support 4 decimal places
    sentiment_type = models.CharField(max_length=20)
    date = models.DateField(max_length=30)
    hour = models.IntegerField()
    minute = models.IntegerField()
    emotions = models.CharField(max_length=30)
    device_type = models.CharField(max_length=30)
