# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': '\u0438\u043d\u0444\u043e \u043f\u043e\u043b\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u044f', 'verbose_name_plural': '\u0438\u043d\u0444\u043e \u043f\u043e\u043b\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0435\u0439'},
        ),
        migrations.AlterField(
            model_name='information',
            name='can_book',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xbc\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x82 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xbd\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='information',
            name='phone_number',
            field=models.IntegerField(verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='information',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
            preserve_default=True,
        ),
    ]
