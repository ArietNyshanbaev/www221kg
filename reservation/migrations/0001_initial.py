# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(max_length=250, verbose_name=b'\xd0\xb7\xd0\xb0\xd0\xb1\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f')),
                ('date_time', models.DateField(verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0')),
                ('time_booked', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h9_00', models.BooleanField(default=False, verbose_name=b'09:00-09:30')),
                ('h9_30', models.BooleanField(default=False, verbose_name=b'09:30-10:00')),
                ('h10_00', models.BooleanField(default=False, verbose_name=b'10:00-10:30')),
                ('h10_30', models.BooleanField(default=False, verbose_name=b'10:30-11:00')),
                ('h11_00', models.BooleanField(default=False, verbose_name=b'11:00-11:30')),
                ('h11_30', models.BooleanField(default=False, verbose_name=b'11:30-12:00')),
                ('h12_00', models.BooleanField(default=False, verbose_name=b'12:00-12:30')),
                ('h12_30', models.BooleanField(default=False, verbose_name=b'12:30-13:00')),
                ('h13_00', models.BooleanField(default=False, verbose_name=b'13:00-13:30')),
                ('h13_30', models.BooleanField(default=False, verbose_name=b'13:30-14:00')),
                ('h14_00', models.BooleanField(default=False, verbose_name=b'14:00-14:30')),
                ('h14_30', models.BooleanField(default=False, verbose_name=b'14:30-15:00')),
                ('h15_00', models.BooleanField(default=False, verbose_name=b'15:00-15:30')),
                ('h15_30', models.BooleanField(default=False, verbose_name=b'15:30-16:00')),
                ('h16_00', models.BooleanField(default=False, verbose_name=b'16:00-16:30')),
                ('h16_30', models.BooleanField(default=False, verbose_name=b'16:30-17:00')),
                ('h17_00', models.BooleanField(default=False, verbose_name=b'17:00-17:30')),
                ('h17_30', models.BooleanField(default=False, verbose_name=b'17:30-18:00')),
                ('h18_00', models.BooleanField(default=False, verbose_name=b'18:00-18:30')),
                ('h18_30', models.BooleanField(default=False, verbose_name=b'18:30-19:00')),
                ('h19_00', models.BooleanField(default=False, verbose_name=b'19:00-19:30')),
                ('h19_30', models.BooleanField(default=False, verbose_name=b'19:30-20:00')),
                ('h20_00', models.BooleanField(default=False, verbose_name=b'20:00-20:30')),
                ('h20_30', models.BooleanField(default=False, verbose_name=b'20:30-21:00')),
                ('h21_00', models.BooleanField(default=False, verbose_name=b'21:00-21:30')),
                ('h21_30', models.BooleanField(default=False, verbose_name=b'21:30-22:00')),
                ('h22_00', models.BooleanField(default=False, verbose_name=b'22:00-22:30')),
                ('h22_30', models.BooleanField(default=False, verbose_name=b'22:30-23:00')),
                ('h23_00', models.BooleanField(default=False, verbose_name=b'23:00-23:30')),
                ('h23_30', models.BooleanField(default=False, verbose_name=b'23:30-00:00')),
                ('h24_00', models.BooleanField(default=False, verbose_name=b'00:00-00:30')),
                ('h24_30', models.BooleanField(default=False, verbose_name=b'00:30-01:00')),
                ('weather', models.TextField(default=b'\xd0\xb7\xd0\xb4\xd0\xb5\xd1\x81\xd1\x8c \xd0\xb4\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xbd\xd0\xb0 \xd0\xb1\xd1\x8b\xd1\x82\xd1\x8c \xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbe \xd0\xbf\xd0\xbe\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb5', verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0')),
                ('day_of_week', models.CharField(max_length=50, verbose_name=b'\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb8')),
                ('date', models.DateField(verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0434\u0435\u043d\u044c',
                'verbose_name_plural': '\u0434\u043d\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image1', models.ImageField(upload_to=b'media', verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe1')),
                ('image2', models.ImageField(upload_to=b'media', verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe2')),
                ('image3', models.ImageField(upload_to=b'media', verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe3')),
                ('image4', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe4', blank=True)),
                ('image5', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe5', blank=True)),
                ('map_image', models.ImageField(upload_to=b'media', verbose_name=b'\xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0')),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('width', models.IntegerField(verbose_name=b'\xd1\x88\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0')),
                ('height', models.IntegerField(verbose_name=b'\xd0\xb4\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0')),
                ('price_usual', models.IntegerField(verbose_name=b'\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb2\xd0\xb5\xd1\x87\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbc')),
                ('price_low', models.IntegerField(verbose_name=b'\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb4\xd0\xbd\xd0\xb5\xd0\xbc')),
                ('address', models.CharField(max_length=250, verbose_name=b'\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('shower', models.BooleanField(default=False, verbose_name=b'\xd0\xb4\xd1\x83\xd1\x88')),
                ('changing_room', models.BooleanField(default=False, verbose_name=b'\xd1\x80\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xb2\xd0\xb0\xd0\xbb\xd0\xba\xd0\xb0')),
                ('wc', models.BooleanField(default=False, verbose_name=b'\xd1\x82\xd1\x83\xd0\xb0\xd0\xbb\xd0\xb5\xd1\x82')),
                ('note1', models.TextField(null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f1', blank=True)),
                ('note2', models.TextField(null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f2', blank=True)),
                ('note3', models.TextField(null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f3', blank=True)),
                ('owner', models.ForeignKey(verbose_name=b'\xd0\xb2\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x86', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u043f\u043e\u043b\u0435',
                'verbose_name_plural': '\u043f\u043e\u043b\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='day',
            name='field',
            field=models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5', to='reservation.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='field',
            field=models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5', to='reservation.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
