from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

# Create your models here.
class League(models.Model):
	"""League class is the class which represents football Leagues"""
	name = models.CharField(max_length = 100)
	eng_name = models.CharField(max_length = 100)
	slogan = models.CharField(max_length = 300)
	image1 = models.ImageField(upload_to = 'media/league')
	image2 = models.ImageField(upload_to = 'media/league')
	image3 = models.ImageField(upload_to = 'media/league')
	
	def __unicode__(self):
		return self.eng_name

class Team(models.Model):
	"""Team class is the class which represents football Team"""
	name = models.CharField(max_length = 100)
	eng_name = models.CharField(max_length = 100)
	slogan = models.CharField(max_length = 300)
	league = models.ForeignKey(League)
	image1 = models.ImageField(upload_to = 'media/team')
	image2 = models.ImageField(upload_to = 'media/team')
	image3 = models.ImageField(upload_to = 'media/team')

	def __unicode__(self):
		return self.eng_name

class News(models.Model):
	"""News class is the class which represents news for particular Team"""
	image = models.ImageField(upload_to = 'media/news',null=True, blank=True)
	date = models.DateTimeField(default=datetime.now)
	team = models.ForeignKey(Team)
	title = models.CharField(max_length = 200, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.title


	
		