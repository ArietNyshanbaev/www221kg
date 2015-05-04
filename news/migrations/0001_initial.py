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
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('eng_name', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=300)),
                ('image1', models.ImageField(upload_to=b'media/league')),
                ('image2', models.ImageField(upload_to=b'media/league')),
                ('image3', models.ImageField(upload_to=b'media/league')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'media/news', blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('eng_name', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=300)),
                ('image1', models.ImageField(upload_to=b'media/team')),
                ('image2', models.ImageField(upload_to=b'media/team')),
                ('image3', models.ImageField(upload_to=b'media/team')),
                ('league', models.ForeignKey(to='news.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='news',
            name='team',
            field=models.ForeignKey(to='news.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
