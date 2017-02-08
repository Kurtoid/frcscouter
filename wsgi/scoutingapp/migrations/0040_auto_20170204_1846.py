# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0039_match_auto_high_goal_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldsetup',
            name='defense2',
        ),
        migrations.RemoveField(
            model_name='fieldsetup',
            name='defense3',
        ),
        migrations.RemoveField(
            model_name='fieldsetup',
            name='defense4',
        ),
        migrations.RemoveField(
            model_name='fieldsetup',
            name='defense5',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='field_setup',
        ),
        migrations.RemoveField(
            model_name='match',
            name='auto_defense_crossed',
        ),
        migrations.AddField(
            model_name='match',
            name='auto_move_yn',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='auto_score_gear_yn',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='auto_trigger_hopper',
            field=models.DecimalField(default=0, max_digits=1, decimal_places=0),
        ),
        migrations.DeleteModel(
            name='FieldSetup',
        ),
    ]
