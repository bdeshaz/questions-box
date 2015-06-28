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
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def score(self):
        s = self.upvote.all().count() * 5
        s -= self.downvote.all().count() * 2
        return s

    def balance(self):
        s = self.upvote.all().count()
        s -= self.downvote.all().count()
        return s

    def set_show(self, u):
        def set_show_on_item(item, user):
            if u is None:
                item.show = False
            elif u in [v.voter for v in item.upvote.all()]:
                item.show = False
            else:
                item.show = True
            item.save()

        set_show_on_item(self, u)
        for c in self.comment.all():
            set_show_on_item(c, u)
        for a in self.answer_set.all():
            set_show_on_item(a, u)
            for c in a.comment.all():
                set_show_on_item(c, u)


    def has_upvoted(self, u):
        if u is None:
            return True
        elif u in [v.voter for v in self.upvote.all()]:
            return True
        else:
            return False


class QuestionComment(GenericEntry):
    parent = models.ForeignKey(Question, related_name="comment",
                                related_query_name="comment_set")
    show = models.BooleanField(default=True)


class QuestionCommentUpvote(models.Model):
    parent = models.ForeignKey(QuestionComment, related_name="upvote")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class QuestionUpvote(models.Model):
    parent = models.ForeignKey(Question, related_name="upvote",
                                related_query_name="upvote_set")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class QuestionDownvote(models.Model):
    parent = models.ForeignKey(Question, related_name="downvote",
                                related_query_name="downvote_set")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)

# Answer classes
class Answer(GenericEntry):
    parent = models.ForeignKey(Question)
    show = models.BooleanField(default=True)

    def score(self):
        s = self.upvote.all().count() * 5
        s -= self.downvote.all().count() * 2
        return s


    def balance(self):
        s = self.upvote.all().count()
        s -= self.downvote.all().count()
        return s


class AnswerComment(GenericEntry):
    parent = models.ForeignKey(Answer, related_name="comment",
                                related_query_name="comment_set")
    show = models.BooleanField(default=True)


class AnswerCommentUpvote(models.Model):
    parent = models.ForeignKey(AnswerComment, related_name="upvote")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class AnswerUpvote(models.Model):
    parent = models.ForeignKey(Answer, related_name="upvote",
                                related_query_name="upvote_set")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)


class AnswerDownvote(models.Model):
    parent = models.ForeignKey(Answer, related_name="downvote",
                                related_query_name="downvote_set")
    voter = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now=True)
