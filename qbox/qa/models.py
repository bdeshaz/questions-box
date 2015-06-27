from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime
import pytz

# Create your models here.


class GenericEntry(models.Model): # parent class for Q & A
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    # relationships
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True


class GenericUpvote(models.Model):
    voter = models.PrimaryKey(User)
    posted_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class GenericDownvote(models.Model):
    voter = models.PrimaryKey(User)
    posted_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# begin class declaration
class Tag(models.Model):
    text = models.CharField(max_length=255)


class Comment(GenericEntry):
    voter = models.ManyToManyField(User, related_name="voted_comment")


class CommentUpvote(GenericUpvote):
    parent = models.PrimaryKey(Comment)


class Question(GenericEntry):
    title = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)
    # voter = models.ManyToManyField(User, related_name="voted_question")
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title

    def score(self):
        s = self.questionupvote_set.count() * 5
        s -= self.questiondownvote_set.count() * 2
        return s


class QuestionUpvote(GenericUpvote):
    parent = models.PrimaryKey(Question)


class QuestionDownvote(GenericDownvote):
    parent = models.PrimaryKey(Question)


class Answer(GenericEntry):
    parent_question = models.ForeignKey(Question)
    # voter = models.ManyToManyField(User, related_name="voted_answer")
    comments = models.ManyToManyField(Comment)

    def score(self):
        s = self.answerupvote_set.count() * 10
        s -= self.answerdownvote_set.count() * 2
        return s



class AnswerUpvote(GenericUpvote):
    parent = models.PrimaryKey(Answer)


class AnswerDownvote(GenericDownvote):
    parent = models.PrimaryKey(Answer)
