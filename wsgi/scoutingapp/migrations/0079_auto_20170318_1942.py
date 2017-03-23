# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0078_match_gears_dropped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_1_rope_1_engaged',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p1r1', to='scoutingapp.RopeType'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_1_rope_2_engaged',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p1r2', to='scoutingapp.RopeType'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_1_rope_3_engaged',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p1r3', to='scoutingapp.RopeType'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_1_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p1team', to='scoutingapp.Team'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_2_rope_1_engaged',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p2r1', to='scoutingapp.RopeType'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_2_rope_2_engaged',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p2r2', to='scoutingapp.RopeType'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_2_rope_3_engaged',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p2r3', to='scoutingapp.RopeType'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_2_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p2team', to='scoutingapp.Team'),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='scouted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='robot_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Robot1card', to='scoutingapp.Card'),
        ),
        migrations.AlterField(
            model_name='match',
            name='robot_end_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='robot1endgame', to='scoutingapp.EndGameState'),
        ),
        migrations.AlterField(
            model_name='match',
            name='scouted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scoutingapp.Tournament'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scoutingapp.Team'),
        ),
    ]
