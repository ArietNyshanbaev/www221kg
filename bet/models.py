from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Tour(models.Model):
    tour_number = models.IntegerField('номер тура', primary_key=True)
    tour_end = models.CharField('ставки берутся до', max_length=100)
    tour_prize = models.CharField('приз тура', max_length=50)
    tour_note1 = models.CharField('примечание1', max_length=100,blank=True,null=True)
    tour_note2 = models.CharField('примечание2', max_length=100,blank=True,null=True)
    tour_note3 = models.CharField('примечание3', max_length=100,blank=True,null=True)
    
    def __unicode__(self):
        return str(self.tour_number)

    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'тура'

class Match(models.Model):
    tour = models.ForeignKey(Tour, verbose_name='тур')
    first_team = models.CharField('первая команда', max_length = 62)
    second_team = models.CharField('вторая команда', max_length = 62)
    goal_first = models.IntegerField('голы первой команды', default = 0)
    goal_second = models.IntegerField('голы второй команды', default = 0)
    def __unicode__(self):
        return self.first_team + " vs " + self.second_team

    class Meta:
        verbose_name = 'матч'
        verbose_name_plural = 'матчи'
    
class Bet(models.Model):
    user = models.ForeignKey(User, verbose_name='ползователь')
    tour_number = models.IntegerField('номер тура', default = 0)
    correct_num = models.IntegerField('правильные исходы', default = 0)
    date = models.DateTimeField('дата ставки', default=datetime.now)
    match1 = models.IntegerField('матч1')
    match2 = models.IntegerField('матч2')
    match3 = models.IntegerField('матч3')
    match4 = models.IntegerField('матч4')
    match5 = models.IntegerField('матч5')
    match6 = models.IntegerField('матч6')
    match7 = models.IntegerField('матч7')
    match8 = models.IntegerField('матч8')
    match9 = models.IntegerField('матч9')
    match10 = models.IntegerField('матч10')
    
    def __unicode__(self):
        return str(self.user) +" "+ str(self.tour_number)

    class Meta:
        verbose_name = 'ставка'
        verbose_name_plural = 'ставки'


class CurrentTour(models.Model):
    tour_number = models.IntegerField('номер тура', default = 1)
    
    def __unicode__(self):
        return str(self.tour_number)

    class Meta:
        verbose_name = 'номер тура этой недели'
        verbose_name_plural = 'номер тура этой недели'
        
        
        
