import datetime

from django.db import models
from django.utils import timezone
from mongoengine import Document, fields

# Create your models here.
class Question(Document):
    question_text = fields.StringField(max_length=200)
    pub_date = fields.DateTimeField('date published')
    
    def __str__(self):
        """ Prints the question text as a 
        representation of the object"""
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = fields.ReferenceField(Question)
    choice_text = fields.StringField(max_length=200)
    votes = fields.IntField(default=0)
    
    def __str__(self):
        """ Prints the text of this choice as a 
        representation of the object"""
        return self.choice_text