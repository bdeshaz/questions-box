from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime
import pytz

# Create your models here.

class Tag(models.Model):
    text = models.CharField(max_length=255)


class GenericEntry(models.Model): # parent class for Q & A
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    # relationships
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True


class Question(GenericEntry):
    title = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)
    voter = models.ManyToManyField(User, related_name="voted_question")


class Answer(GenericEntry):
    parent_question = models.ForeignKey(Question)
    voter = models.ManyToManyField(User, related_name="voted_answer")


class Comment(GenericEntry):
    # can be on answer OR question
    on_answer = models.BooleanField(default=True)
    parent_answer = models.ForeignKey(Answer, null=True)
    parent_question = models.ForeignKey(Question, null=True)
    voter = models.ManyToManyField(User, related_name="voted_comment")



# class Score(models.Model):
#     score = models.IntegerField()
#     question = models.ForeignKey(Question)
#     answer = models.ForeignKey(Answers)
#     user = models.ForeignKey(User)
