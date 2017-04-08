# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0086_auto_20170323_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alliancematch',
            old_name='pilot_rope_1_engaged',
            new_name='pilot_rope_deploy_time',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_rope_2_engaged',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_rope_3_engaged',
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_card',
            field=models.ForeignKey(related_name='pilot1card', on_delete=django.db.models.deletion.SET_NULL, to='scoutingapp.Card', blank=True, null=True),
        ),
    ]
