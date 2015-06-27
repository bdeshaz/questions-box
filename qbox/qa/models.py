from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime
import pytz

# Abstract classes
class GenericEntry(models.Model): # parent class for Q & A
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    # relationships
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True

# begin class declaration
class Tag(models.Model):
    text = models.CharField(max_length=255)


# Question classes
class Question(GenericEntry):
    title = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def score(self):
        # return 0
        if self.upvote_set is None:
            return 0
        else:
            s = self.upvote_set.count() * 5
            s -= self.downvote_set.count() * 2

            # s = self.questionupvote_set.count() * 5
            # s -= self.questiondownvote_set.count() * 2
            return s


class QuestionComment(GenericEntry):
    parent = models.ForeignKey(Question, related_name="comment", related_query_name="comment_set")


class QuestionCommentUpvote(models.Model):
    parent = models.ForeignKey(QuestionComment, related_name="upvote")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class QuestionUpvote(models.Model):
    parent = models.ForeignKey(Question, related_name="upvote", related_query_name="upvote_set")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class QuestionDownvote(models.Model):
    parent = models.ForeignKey(Question, related_name="downvote")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)

# Answer classes
class Answer(GenericEntry):
    parent = models.ForeignKey(Question)

    def score(self):
        s = self.answerupvote_set.count() * 10
        s -= self.answerdownvote_set.count() * 2
        return s


class AnswerComment(GenericEntry):
    parent = models.ForeignKey(Answer, related_name="comment", related_query_name="comment_set")


class AnswerCommentUpvote(models.Model):
    parent = models.ForeignKey(AnswerComment, related_name="upvote")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class AnswerUpvote(models.Model):
    parent = models.ForeignKey(Answer, related_name="upvote", related_query_name="upvote_set")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class AnswerDownvote(models.Model):
    parent = models.ForeignKey(Answer, related_name="downvote")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)
