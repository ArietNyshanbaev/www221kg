#import python packeges and files
from datetime import datetime
#import django packeges and files
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Information(models.Model):
	"""This is class which stores all information about particular user"""

	user = models.OneToOneField(User,primary_key=True)
	phone_number = models.IntegerField()
	can_book = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username
	 
	