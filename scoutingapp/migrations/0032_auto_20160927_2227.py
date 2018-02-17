# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0031_auto_20160917_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_1_end_game',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_2_end_game',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_3_end_game',
        ),
        migrations.AddField(
            model_name='match',
            name='robot_1_end_game',
            field=models.ForeignKey(null=True, to='scoutingapp.EndGameState', related_name='robot1endgame'),
        ),
    ]
