# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_eng_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(default=b"here we have news's body"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default=b'here we have short description of news'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='eng_title',
            field=models.CharField(default=b'Title of news goes here', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default=b'Title of news goes here', max_length=200),
            preserve_default=True,
        ),
    ]
