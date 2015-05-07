# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='field',
        ),
        migrations.RemoveField(
            model_name='bookrequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='BookRequest',
        ),
        migrations.RemoveField(
            model_name='day',
            name='field',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.RemoveField(
            model_name='field',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
    ]
