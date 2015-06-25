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


class Answers(models.Model):
	text = models.TextField()
	posted_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
	text = models.TextField(max_length=255)


class Tags(models.Model):
	text = models.CharField(max_length=255)
