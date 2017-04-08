# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0095_auto_20170324_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='preloadedgearaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 4, 8, 20, 0, 7, 163805)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preloadedgearaction',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 8, 20, 0, 12, 497949), auto_now=True),
            preserve_default=False,
        ),
    ]
