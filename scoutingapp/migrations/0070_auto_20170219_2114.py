# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0069_match_duplicate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='auto_trigger_hopper',
            new_name='auto_hoppers_triggered',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='auto_low_efficiency_load',
            new_name='auto_low_goal_accuracy',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='trigger_hopper',
            new_name='teleop_hoppers_triggered',
        ),
        migrations.RemoveField(
            model_name='match',
            name='auto_high_efficiency_load',
        ),
        migrations.AddField(
            model_name='match',
            name='auto_high_goal_accuracy',
            field=models.ForeignKey(related_name='auto_high_goal_accuracy', to='scoutingapp.HighEfficiency', null=True),
        ),
    ]
