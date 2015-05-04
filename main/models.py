#import python packeges and files
from datetime import datetime
#import django packeges and files
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Information(models.Model):
	"""This is class which stores all information about particular user"""

	user = models.OneToOneField(User,primary_key=True, verbose_name='ползователь')
	phone_number = models.IntegerField('номер телефона')
	can_book = models.BooleanField('может бронировать', default=False)

	def __unicode__(self):
		return self.user.first_name +" "+ self.user.last_name

	class Meta:
		verbose_name = "инфо ползователья"
		verbose_name_plural = "инфо ползовательей"