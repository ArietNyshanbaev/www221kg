# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bet',
            options={'verbose_name': '\u0441\u0442\u0430\u0432\u043a\u0430', 'verbose_name_plural': '\u0441\u0442\u0430\u0432\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='currenttour',
            options={'verbose_name': '\u043d\u043e\u043c\u0435\u0440 \u0442\u0443\u0440\u0430 \u044d\u0442\u043e\u0439 \u043d\u0435\u0434\u0435\u043b\u0438', 'verbose_name_plural': '\u043d\u043e\u043c\u0435\u0440 \u0442\u0443\u0440\u0430 \u044d\u0442\u043e\u0439 \u043d\u0435\u0434\u0435\u043b\u0438'},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': '\u043c\u0430\u0442\u0447', 'verbose_name_plural': '\u043c\u0430\u0442\u0447\u0438'},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': '\u0442\u0443\u0440', 'verbose_name_plural': '\u0442\u0443\u0440\u0430'},
        ),
        migrations.RemoveField(
            model_name='match',
            name='result',
        ),
        migrations.AlterField(
            model_name='bet',
            name='correct_num',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb8\xd1\x81\xd1\x85\xd0\xbe\xd0\xb4\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match1',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x871'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match10',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x8710'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match2',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x872'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match3',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x873'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match4',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x874'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match5',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x875'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match6',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x876'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match7',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x877'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match8',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x878'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match9',
            field=models.IntegerField(verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd1\x879'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='tour_number',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='currenttour',
            name='tour_number',
            field=models.IntegerField(default=1, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='first_team',
            field=models.CharField(max_length=60, verbose_name=b'\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb0\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='goal_first',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xbb\xd1\x8b \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='goal_second',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xbb\xd1\x8b \xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='second_team',
            field=models.CharField(max_length=60, verbose_name=b'\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='tour',
            field=models.ForeignKey(verbose_name=b'\xd1\x82\xd1\x83\xd1\x80', to='bet.Tour'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_end',
            field=models.CharField(max_length=100, verbose_name=b'\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8 \xd0\xb1\xd0\xb5\xd1\x80\xd1\x83\xd1\x82\xd1\x81\xd1\x8f \xd0\xb4\xd0\xbe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_note1',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb51', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_note2',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb52', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_note3',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb53', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_number',
            field=models.IntegerField(serialize=False, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_prize',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb7 \xd1\x82\xd1\x83\xd1\x80\xd0\xb0'),
            preserve_default=True,
        ),
    ]
