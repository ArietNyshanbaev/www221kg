# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_eng_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='eng_title',
        ),
    ]
