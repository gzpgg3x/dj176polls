import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # question = models.charfield(max_length=128, unique=true)
    question_text = models.CharField(max_length=200)
    # pub_date = models.datefield
    # pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date published')    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        # return self.was_published_recently = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
        now = timezone.now()
        return now -datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean =  True
    was_published_recently.short_description = 'Published recently?'       

class Choice(models.Model):
    question = models.ForeignKey(Question)
    # vote = models.boolean()
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text




