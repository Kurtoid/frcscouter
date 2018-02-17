# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0083_auto_20170321_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='auto_hoppers_triggered',
            new_name='auto_hopper_triggered',
        ),
        migrations.RemoveField(
            model_name='match',
            name='auto_high_goal_accuracy',
        ),
        migrations.RemoveField(
            model_name='match',
            name='auto_hopper_load',
        ),
        migrations.RemoveField(
            model_name='match',
            name='auto_low_goal_accuracy',
        ),
    ]
