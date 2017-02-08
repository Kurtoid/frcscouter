# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0035_remove_match_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='auto_high_balls',
            new_name='auto_high_goal',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='auto_low_balls',
            new_name='auto_low_goal',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='high_balls_goals_made',
            new_name='high_goals_scored',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_1_card',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_2_card',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_3_card',
        ),
        migrations.AddField(
            model_name='match',
            name='robot_card',
            field=models.ForeignKey(related_name='Robot1card', null=True, to='scoutingapp.Card'),
        ),
    ]
