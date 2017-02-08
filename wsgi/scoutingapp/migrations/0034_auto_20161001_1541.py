# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0033_auto_20161001_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='dropped_balls',
            new_name='dropped_boulders',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='high_balls',
            new_name='high_balls_goals_made',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='high_balls_missed',
            new_name='high_goals_missed',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='low_balls',
            new_name='low_goals_scored',
        ),
    ]
