from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Field(models.Model):
    image1 = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    image3 = models.ImageField(upload_to='media')
    image4 = models.ImageField(upload_to='media')
    image5 = models.ImageField(upload_to='media')
    map_image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=200)
    width = models.IntegerField()
    height = models.IntegerField()
    price_usual = models.IntegerField()
    price_low = models.IntegerField()
    address = models.CharField(max_length=250)
    shower = models.BooleanField(default=False)
    changing_room = models.BooleanField(default=False)
    wc = models.BooleanField(default=False)
    note1 = models.TextField(blank=True, null=True)
    note2 = models.TextField(blank=True, null=True)
    note3 = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Day(models.Model):
    h9_00 = models.BooleanField(default=False)
    h9_30 = models.BooleanField(default=False)
    h10_00 = models.BooleanField(default=False)
    h10_30 = models.BooleanField(default=False)
    h11_00 = models.BooleanField(default=False)
    h11_30 = models.BooleanField(default=False)
    h12_00 = models.BooleanField(default=False)
    h12_30 = models.BooleanField(default=False)
    h13_00 = models.BooleanField(default=False)
    h13_30 = models.BooleanField(default=False)
    h14_00 = models.BooleanField(default=False)
    h14_30 = models.BooleanField(default=False)
    h15_00 = models.BooleanField(default=False)
    h15_30 = models.BooleanField(default=False)
    h16_00 = models.BooleanField(default=False)
    h16_30 = models.BooleanField(default=False)
    h17_00 = models.BooleanField(default=False)
    h17_30 = models.BooleanField(default=False)
    h18_00 = models.BooleanField(default=False)
    h18_30 = models.BooleanField(default=False)
    h19_00 = models.BooleanField(default=False)
    h19_30 = models.BooleanField(default=False)
    h20_00 = models.BooleanField(default=False)
    h20_30 = models.BooleanField(default=False)
    h21_00 = models.BooleanField(default=False)
    h21_30 = models.BooleanField(default=False)
    h22_00 = models.BooleanField(default=False)
    h22_30 = models.BooleanField(default=False)
    h23_00 = models.BooleanField(default=False)
    h23_30 = models.BooleanField(default=False)
    h24_00 = models.BooleanField(default=False)
    h24_30 = models.BooleanField(default=False)

    weather = models.TextField(default="here we have some weather information")
    field = models.ForeignKey(Field)
    day_of_week = models.CharField(max_length = 50)
    date = models.DateField()
    
    def __unicode__(self):
        return self.day_of_week +" of "+ str(self.field)
    
    
class BookRequest(models.Model):
    user = models.ForeignKey(User)
    time = models.CharField(max_length = 250)
    date_time = models.DateField()
    field = models.ForeignKey(Field)
    time_booked = models.DateTimeField(default=datetime.now)
    
    def __unicode__(self):
        return self.user.username + ' ' + str(self.field.name) + ' ' + str(self.date_time)

from django.db import models

# Create your models here.
