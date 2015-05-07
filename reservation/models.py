from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Field(models.Model):
    image1 = models.ImageField('фото1', upload_to='media')
    image2 = models.ImageField('фото2', upload_to='media')
    image3 = models.ImageField('фото3', upload_to='media')
    image4 = models.ImageField('фото4', upload_to='media', null=True, blank=True)
    image5 = models.ImageField('фото5', upload_to='media', null=True, blank=True)
    map_image = models.ImageField('карта', upload_to='media')
    owner = models.ForeignKey(User, verbose_name='владелец')
    name = models.CharField('название', max_length=200)
    width = models.IntegerField('ширина')
    height = models.IntegerField('длина')
    price_usual = models.IntegerField('цена вечером')
    price_low = models.IntegerField('цена днем')
    address = models.CharField('адрес', max_length=250)
    shower = models.BooleanField('душ', default=False)
    changing_room = models.BooleanField('раздевалка', default=False)
    wc = models.BooleanField('туалет', default=False)
    note1 = models.TextField('примечания1', blank=True, null=True)
    note2 = models.TextField('примечания2', blank=True, null=True)
    note3 = models.TextField('примечания3', blank=True, null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'поле'
        verbose_name_plural = 'поля'

class Day(models.Model):
    h9_00 = models.BooleanField('09:00-09:30', default=False)
    h9_30 = models.BooleanField('09:30-10:00', default=False)
    h10_00 = models.BooleanField('10:00-10:30', default=False)
    h10_30 = models.BooleanField('10:30-11:00', default=False)
    h11_00 = models.BooleanField('11:00-11:30', default=False)
    h11_30 = models.BooleanField('11:30-12:00', default=False)
    h12_00 = models.BooleanField('12:00-12:30', default=False)
    h12_30 = models.BooleanField('12:30-13:00', default=False)
    h13_00 = models.BooleanField('13:00-13:30', default=False)
    h13_30 = models.BooleanField('13:30-14:00', default=False)
    h14_00 = models.BooleanField('14:00-14:30', default=False)
    h14_30 = models.BooleanField('14:30-15:00', default=False)
    h15_00 = models.BooleanField('15:00-15:30', default=False)
    h15_30 = models.BooleanField('15:30-16:00', default=False)
    h16_00 = models.BooleanField('16:00-16:30', default=False)
    h16_30 = models.BooleanField('16:30-17:00', default=False)
    h17_00 = models.BooleanField('17:00-17:30', default=False)
    h17_30 = models.BooleanField('17:30-18:00', default=False)
    h18_00 = models.BooleanField('18:00-18:30', default=False)
    h18_30 = models.BooleanField('18:30-19:00', default=False)
    h19_00 = models.BooleanField('19:00-19:30', default=False)
    h19_30 = models.BooleanField('19:30-20:00', default=False)
    h20_00 = models.BooleanField('20:00-20:30', default=False)
    h20_30 = models.BooleanField('20:30-21:00', default=False)
    h21_00 = models.BooleanField('21:00-21:30', default=False)
    h21_30 = models.BooleanField('21:30-22:00', default=False)
    h22_00 = models.BooleanField('22:00-22:30', default=False)
    h22_30 = models.BooleanField('22:30-23:00', default=False)
    h23_00 = models.BooleanField('23:00-23:30', default=False)
    h23_30 = models.BooleanField('23:30-00:00', default=False)
    h24_00 = models.BooleanField('00:00-00:30', default=False)
    h24_30 = models.BooleanField('00:30-01:00', default=False)

    weather = models.TextField('погода', default='здесь должна быть информация о погоде')
    field = models.ForeignKey(Field, verbose_name='поле')
    day_of_week = models.CharField('день недели', max_length = 50)
    date = models.DateField('дата')
    
    def __unicode__(self):
        return self.day_of_week +" of "+ str(self.field)

    class Meta:
        verbose_name = 'день'
        verbose_name_plural = 'дни'
    
class BookRequest(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь')
    time = models.CharField('забранированное время', max_length = 250)
    date_time = models.DateField('дата')
    field = models.ForeignKey(Field, verbose_name='поле')
    time_booked = models.DateTimeField('дата заявки', default=datetime.now)
    
    def __unicode__(self):
        return self.user.username + ' ' + str(self.field.name) + ' ' + str(self.date_time)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
