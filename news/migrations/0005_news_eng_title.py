# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150428_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='eng_title',
            field=models.CharField(default=b'Title of news goes here', max_length=200),
            preserve_default=True,
        ),
    ]
