# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0079_auto_20170318_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliancematch',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='scoutingapp.Tournament', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='currently_in_event',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='event_code',
            field=models.CharField(max_length=200, default='UNAMED'),
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_dropped',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_scored',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_type',
            field=models.CharField(max_length=100, verbose_name='Gear Source'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=100, default='', null=True),
        ),
    ]
