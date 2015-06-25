from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime
import pytz

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    upvoter = models.ManyToManyField(User, unique=True)



class Answers(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)


class Comment(models.Model):
    text = models.TextField(max_length=255)
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answers)


class Tags(models.Model):
    text = models.CharField(max_length=255)


class Score(models.Model):
    score = models.IntegerField()
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answers)
    user = models.ForeignKey(User)
