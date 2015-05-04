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
                ('time', models.CharField(max_length=250)),
                ('date_time', models.DateField()),
                ('time_booked', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h9_00', models.BooleanField(default=False)),
                ('h9_30', models.BooleanField(default=False)),
                ('h10_00', models.BooleanField(default=False)),
                ('h10_30', models.BooleanField(default=False)),
                ('h11_00', models.BooleanField(default=False)),
                ('h11_30', models.BooleanField(default=False)),
                ('h12_00', models.BooleanField(default=False)),
                ('h12_30', models.BooleanField(default=False)),
                ('h13_00', models.BooleanField(default=False)),
                ('h13_30', models.BooleanField(default=False)),
                ('h14_00', models.BooleanField(default=False)),
                ('h14_30', models.BooleanField(default=False)),
                ('h15_00', models.BooleanField(default=False)),
                ('h15_30', models.BooleanField(default=False)),
                ('h16_00', models.BooleanField(default=False)),
                ('h16_30', models.BooleanField(default=False)),
                ('h17_00', models.BooleanField(default=False)),
                ('h17_30', models.BooleanField(default=False)),
                ('h18_00', models.BooleanField(default=False)),
                ('h18_30', models.BooleanField(default=False)),
                ('h19_00', models.BooleanField(default=False)),
                ('h19_30', models.BooleanField(default=False)),
                ('h20_00', models.BooleanField(default=False)),
                ('h20_30', models.BooleanField(default=False)),
                ('h21_00', models.BooleanField(default=False)),
                ('h21_30', models.BooleanField(default=False)),
                ('h22_00', models.BooleanField(default=False)),
                ('h22_30', models.BooleanField(default=False)),
                ('h23_00', models.BooleanField(default=False)),
                ('h23_30', models.BooleanField(default=False)),
                ('h24_00', models.BooleanField(default=False)),
                ('h24_30', models.BooleanField(default=False)),
                ('weather', models.TextField(default=b'here we have some weather information')),
                ('day_of_week', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image1', models.ImageField(upload_to=b'media')),
                ('image2', models.ImageField(upload_to=b'media')),
                ('image3', models.ImageField(upload_to=b'media')),
                ('image4', models.ImageField(upload_to=b'media')),
                ('image5', models.ImageField(upload_to=b'media')),
                ('map_image', models.ImageField(upload_to=b'media')),
                ('name', models.CharField(max_length=200)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('price_usual', models.IntegerField()),
                ('price_low', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('shower', models.BooleanField(default=False)),
                ('changing_room', models.BooleanField(default=False)),
                ('wc', models.BooleanField(default=False)),
                ('note1', models.TextField(null=True, blank=True)),
                ('note2', models.TextField(null=True, blank=True)),
                ('note3', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='day',
            name='field',
            field=models.ForeignKey(to='reservation.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='field',
            field=models.ForeignKey(to='reservation.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
