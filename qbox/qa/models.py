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
    # vote = models.OneToManyField(Vote)
    # voter = models.ManyToManyField(User)

    class Meta:
        abstract = True


class Question(GenericEntry):
    title = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)


class Answer(GenericEntry):
    parent_question = models.ForeignKey(Question)


class Comment(GenericEntry):
    # can be on answer OR question
    on_answer = models.BooleanField(default=True)
    parent_answer = models.ForeignKey(Answer)
    parent_question = models.ForeignKey(Question)


class QuestionVote(models.Model):
    question = models.ForeignKey(Question)



# class Score(models.Model):
#     score = models.IntegerField()
#     question = models.ForeignKey(Question)
#     answer = models.ForeignKey(Answers)
#     user = models.ForeignKey(User)
