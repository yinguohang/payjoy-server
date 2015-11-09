'''
from django.db import models
from django.utils import timezone

class Shop(models.Model):
	id = models.IntegerField(primary_key = True)
	grade = models.IntegerField()
	rid = models.IntegerField(blank = True, default = 0)
	updateTime = models.DateTimeField(default = timezone.now)

class Item(models.Model):
	id = models.IntegerField(primary_key = True)
	grade = models.IntegerField()
	goodComment = models.TextField()
	badComment = models.TextField()
	rid = models.IntegerField(blank = True, default = 0)
	updateTime = models.DateTimeField(default = timezone.now)
'''

from mongoengine import *
from mongoengine.fields import *
from django.utils import timezone

class Shop(Document):
	shopId = LongField(required = True, primary_key = True)
	grade = IntField()
	rid = IntField()
	updateTime = DateTimeField(default = timezone.now)
	
class Item(Document):
	itemId = LongField(required = True, primary_key = True)
	grade = IntField()
	rid = IntField()
	updateTime = DateTimeField(default = timezone.now)
	goodComment = ListField()
	badComment = ListField()
	hasComment = BooleanField(default = False)