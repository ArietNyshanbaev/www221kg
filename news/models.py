from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

# Create your models here.
class League(models.Model):
	"""League class is the class which represents football Leagues"""
	name = models.CharField('название', max_length = 100)
	slogan = models.CharField('девиз', max_length = 300)
	image1 = models.ImageField('фото', upload_to = 'media/league')
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'лига'
		verbose_name_plural = 'лиги'

class Team(models.Model):
	"""Team class is the class which represents football Team"""
	name = models.CharField('название', max_length = 100)
	slogan = models.CharField('девиз', max_length = 300)
	league = models.ForeignKey(League, verbose_name='лига')
	image1 = models.ImageField('фото', upload_to = 'media/team')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "команда"
		verbose_name_plural = "команды"

class News(models.Model):
	"""News class is the class which represents news for particular Team"""
	image = models.ImageField('фото', upload_to = 'media/news',null=True, blank=True)
	date = models.DateTimeField('дата' ,default=datetime.now)
	team = models.ForeignKey(Team, verbose_name='команда')
	title = models.CharField('тема', max_length = 200, null=True, blank=True)
	description = models.TextField('короткое изложение', null=True, blank=True)
	body = models.TextField('новость', null=True, blank=True)
	user = models.ForeignKey(User, verbose_name='ползователь')
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "новости"
		verbose_name_plural = "новости"


	
		