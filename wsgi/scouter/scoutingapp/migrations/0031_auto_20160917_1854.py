# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0030_auto_20160917_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliancematch',
            name='robot_1_end_game',
            field=models.ForeignKey(null=True, related_name='robot1endgame', to='scoutingapp.EndGameState'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='robot_2_end_game',
            field=models.ForeignKey(null=True, related_name='robot2endgame', to='scoutingapp.EndGameState'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='robot_3_end_game',
            field=models.ForeignKey(null=True, related_name='robot3endgame', to='scoutingapp.EndGameState'),
        ),
    ]
