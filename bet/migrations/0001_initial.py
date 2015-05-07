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
                ('tour_number', models.IntegerField(default=0, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0')),
                ('correct_num', models.IntegerField(default=0, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb8\xd1\x81\xd1\x85\xd0\xbe\xd0\xb4\xd1\x8b')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8')),
                ('match1', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x871')),
                ('match2', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x872')),
                ('match3', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x873')),
                ('match4', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x874')),
                ('match5', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x875')),
                ('match6', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x876')),
                ('match7', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x877')),
                ('match8', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x878')),
                ('match9', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x879')),
                ('match10', models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x8710')),
                ('user', models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0430\u0432\u043a\u0430',
                'verbose_name_plural': '\u0441\u0442\u0430\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentTour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tour_number', models.IntegerField(default=1, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u043d\u043e\u043c\u0435\u0440 \u0442\u0443\u0440\u0430 \u044d\u0442\u043e\u0439 \u043d\u0435\u0434\u0435\u043b\u0438',
                'verbose_name_plural': '\u043d\u043e\u043c\u0435\u0440 \u0442\u0443\u0440\u0430 \u044d\u0442\u043e\u0439 \u043d\u0435\u0434\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_team', models.CharField(max_length=62, verbose_name=b'\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb0\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0')),
                ('second_team', models.CharField(max_length=62, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0')),
                ('goal_first', models.IntegerField(default=0, verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xbb\xd1\x8b \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b')),
                ('goal_second', models.IntegerField(default=0, verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xbb\xd1\x8b \xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b')),
            ],
            options={
                'verbose_name': '\u043c\u0430\u0442\u0447',
                'verbose_name_plural': '\u043c\u0430\u0442\u0447\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('tour_number', models.IntegerField(serialize=False, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0', primary_key=True)),
                ('tour_end', models.CharField(max_length=100, verbose_name=b'\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8 \xd0\xb1\xd0\xb5\xd1\x80\xd1\x83\xd1\x82\xd1\x81\xd1\x8f \xd0\xb4\xd0\xbe')),
                ('tour_prize', models.CharField(max_length=50, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb7 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0')),
                ('tour_note1', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb51', blank=True)),
                ('tour_note2', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb52', blank=True)),
                ('tour_note3', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb53', blank=True)),
            ],
            options={
                'verbose_name': '\u0442\u0443\u0440',
                'verbose_name_plural': '\u0442\u0443\u0440\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='tour',
            field=models.ForeignKey(verbose_name=b'\xd1\x82\xd1\x83\xd1\x80', to='bet.Tour'),
            preserve_default=True,
        ),
    ]
