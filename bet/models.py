from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Match(models.Model):
    tour = models.ForeignKey('Tour')
    first_team = models.CharField(max_length = 60)
    second_team = models.CharField(max_length = 60)
    result = models.CharField(max_length = 60,default = 'Net stavki')
    goal_first = models.IntegerField(default = 0)
    goal_second = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.first_team + " vs " + self.second_team + " " + str(self.tour)
    
class Bet(models.Model):
    user = models.ForeignKey(User)
    tour_number = models.IntegerField(default = 0)
    correct_num = models.IntegerField(default = 0)
    date = models.DateTimeField(default=datetime.now)
    match1 = models.IntegerField()
    match2 = models.IntegerField()
    match3 = models.IntegerField()
    match4 = models.IntegerField()
    match5 = models.IntegerField()
    match6 = models.IntegerField()
    match7 = models.IntegerField()
    match8 = models.IntegerField()
    match9 = models.IntegerField()
    match10 = models.IntegerField()
    
    def __unicode__(self):
        return str(self.user) +" "+ str(self.tour_number) + "-tour"


class Tour(models.Model):
    tour_number = models.IntegerField(primary_key=True)
    tour_end = models.CharField(max_length=100)
    tour_prize = models.CharField(max_length=50)
    tour_note1 = models.CharField(max_length=100,blank=True,null=True)
    tour_note2 = models.CharField(max_length=100,blank=True,null=True)
    tour_note3 = models.CharField(max_length=100,blank=True,null=True)
    
    def __unicode__(self):
        return 'tour number ' + str(self.tour_number)


class CurrentTour(models.Model):
    tour_number = models.IntegerField(default = 1)
    
    def __unicode__(self):
        return str(self.tour_number)+" "

        
        
        