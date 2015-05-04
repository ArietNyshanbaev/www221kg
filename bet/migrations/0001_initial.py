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
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tour_number', models.IntegerField(default=0)),
                ('correct_num', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('match1', models.IntegerField()),
                ('match2', models.IntegerField()),
                ('match3', models.IntegerField()),
                ('match4', models.IntegerField()),
                ('match5', models.IntegerField()),
                ('match6', models.IntegerField()),
                ('match7', models.IntegerField()),
                ('match8', models.IntegerField()),
                ('match9', models.IntegerField()),
                ('match10', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentTour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tour_number', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_team', models.CharField(max_length=60)),
                ('second_team', models.CharField(max_length=60)),
                ('result', models.CharField(default=b'Net stavki', max_length=60)),
                ('goal_first', models.IntegerField(default=0)),
                ('goal_second', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('tour_number', models.IntegerField(serialize=False, primary_key=True)),
                ('tour_end', models.CharField(max_length=100)),
                ('tour_prize', models.CharField(max_length=50)),
                ('tour_note1', models.CharField(max_length=100, null=True, blank=True)),
                ('tour_note2', models.CharField(max_length=100, null=True, blank=True)),
                ('tour_note3', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='tour',
            field=models.ForeignKey(to='bet.Tour'),
            preserve_default=True,
        ),
    ]
