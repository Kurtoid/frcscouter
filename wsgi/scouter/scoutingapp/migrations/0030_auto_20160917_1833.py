# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0029_auto_20160917_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliancematch',
            name='robot_1_end_game',
            field=models.ForeignKey(default=1, related_name='robot1endgame', to='scoutingapp.EndGameState'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_2_end_game',
            field=models.ForeignKey(default=1, related_name='robot2endgame', to='scoutingapp.EndGameState'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_3_end_game',
            field=models.ForeignKey(default=1, related_name='robot3endgame', to='scoutingapp.EndGameState'),
            preserve_default=False,
        ),
    ]
