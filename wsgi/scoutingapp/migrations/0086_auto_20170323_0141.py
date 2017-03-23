# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0085_auto_20170321_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alliancematch',
            old_name='auto_pilot_1_gears_acquired',
            new_name='auto_pilot_gears_acquired',
        ),
        migrations.RenameField(
            model_name='alliancematch',
            old_name='auto_pilot_1_rotors_engaged',
            new_name='auto_pilot_rotors_engaged',
        ),
        migrations.RenameField(
            model_name='alliancematch',
            old_name='auto_pilot_2_gears_acquired',
            new_name='pilot_gears_acquired',
        ),
        migrations.RenameField(
            model_name='alliancematch',
            old_name='pilot_1_rope_1_engaged',
            new_name='pilot_rope_1_engaged',
        ),
        migrations.RenameField(
            model_name='alliancematch',
            old_name='pilot_1_rope_2_engaged',
            new_name='pilot_rope_2_engaged',
        ),
        migrations.RenameField(
            model_name='alliancematch',
            old_name='pilot_1_rope_3_engaged',
            new_name='pilot_rope_3_engaged',
        ),
        migrations.RenameField(
            model_name='alliancematch',
            old_name='auto_pilot_2_rotors_engaged',
            new_name='pilot_rotors_engaged',
        ),
        migrations.RenameField(
            model_name='alliancematch',
            old_name='pilot_1_team',
            new_name='pilot_team',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_1_gears_acquired',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_1_rotors_engaged',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_2_gears_acquired',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_2_rope_1_engaged',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_2_rope_2_engaged',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_2_rope_3_engaged',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_2_rotors_engaged',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='pilot_2_team',
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='scouter_number',
            field=models.DecimalField(default=0, max_digits=1, decimal_places=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_type',
            field=models.CharField(blank=True, max_length=100, verbose_name='Gear Source'),
        ),
    ]
