# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0081_auto_20170321_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 21, 14, 5, 0, 670623), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 21, 14, 5, 9, 666980), auto_now=True),
            preserve_default=False,
        ),
    ]
