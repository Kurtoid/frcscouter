# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0043_auto_20170204_2145'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HopperEfficiency',
            new_name='HighEfficiency',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='auto_efficiency_load',
            new_name='auto_high_efficiency_load',
        ),
    ]