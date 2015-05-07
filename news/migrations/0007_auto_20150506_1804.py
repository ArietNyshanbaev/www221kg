# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_news_eng_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='league',
            options={'verbose_name': '\u043b\u0438\u0433\u0430', 'verbose_name_plural': '\u043b\u0438\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '\u043d\u043e\u0432\u043e\u0441\u0442\u0438', 'verbose_name_plural': '\u043d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': '\u043a\u043e\u043c\u0430\u043d\u0434\u0430', 'verbose_name_plural': '\u043a\u043e\u043c\u0430\u043d\u0434\u044b'},
        ),
        migrations.RemoveField(
            model_name='league',
            name='eng_name',
        ),
        migrations.RemoveField(
            model_name='league',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='league',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='eng_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image3',
        ),
        migrations.AlterField(
            model_name='league',
            name='image1',
            field=models.ImageField(upload_to=b'media/league', verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='slogan',
            field=models.CharField(max_length=300, verbose_name=b'\xd0\xb4\xd0\xb5\xd0\xb2\xd0\xb8\xd0\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(null=True, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(null=True, verbose_name=b'\xd0\xba\xd0\xbe\xd1\x80\xd0\xbe\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xb8\xd0\xb7\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=b'media/news', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='team',
            field=models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0', to='news.Team'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='image1',
            field=models.ImageField(upload_to=b'media/team', verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.ForeignKey(verbose_name=b'\xd0\xbb\xd0\xb8\xd0\xb3\xd0\xb0', to='news.League'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='slogan',
            field=models.CharField(max_length=300, verbose_name=b'\xd0\xb4\xd0\xb5\xd0\xb2\xd0\xb8\xd0\xb7'),
            preserve_default=True,
        ),
    ]
