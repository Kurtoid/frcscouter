# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0054_auto_20170212_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volley',
            name='high_efficiency_load',
        ),
        migrations.RemoveField(
            model_name='volley',
            name='low_efficiency_load',
        ),
        migrations.RemoveField(
            model_name='volley',
            name='match',
        ),
        migrations.AddField(
            model_name='match',
            name='high_efficiency_load',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='high_efficiency_load', to='scoutingapp.HighEfficiency'),
        ),
        migrations.AddField(
            model_name='match',
            name='hopper_load',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='low_efficiency_load',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='low_efficiency_load', to='scoutingapp.HighEfficiency'),
        ),
        migrations.DeleteModel(
            name='Volley',
        ),
    ]
