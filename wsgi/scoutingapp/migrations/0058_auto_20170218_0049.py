# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0057_auto_20170217_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='gears_aquired',
        ),
        migrations.RemoveField(
            model_name='match',
            name='gears_picked_up',
        ),
        migrations.RemoveField(
            model_name='match',
            name='gears_scored',
        ),
        migrations.RemoveField(
            model_name='match',
            name='high_goals_missed',
        ),
        migrations.RemoveField(
            model_name='match',
            name='high_goals_scored',
        ),
    ]
