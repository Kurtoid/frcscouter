# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0038_auto_20161009_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='auto_high_goal_2',
            field=models.BooleanField(default=False),
        ),
    ]
