# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0070_auto_20170219_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='RopeType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_1_breach_ability',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_1_driver_skill',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_2_breach_ability',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_2_driver_skill',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_3_breach_ability',
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='robot_3_driver_skill',
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_1_gears_acquired',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_1_rotors_engaged',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_2_gears_acquired',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_2_rotors_engaged',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_1_rope_1_engaged',
            field=models.ForeignKey(to='scoutingapp.RopeType', default=1, related_name='p1r1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_1_rope_2_engaged',
            field=models.ForeignKey(to='scoutingapp.RopeType', default=1, related_name='p1r2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_1_rope_3_engaged',
            field=models.ForeignKey(to='scoutingapp.RopeType', default=1, related_name='p1r3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_2_rope_1_engaged',
            field=models.ForeignKey(to='scoutingapp.RopeType', default=1, related_name='p2r1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_2_rope_2_engaged',
            field=models.ForeignKey(to='scoutingapp.RopeType', default=1, related_name='p2r2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_2_rope_3_engaged',
            field=models.ForeignKey(to='scoutingapp.RopeType', default=1, related_name='p2r3'),
            preserve_default=False,
        ),
    ]
