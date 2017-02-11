# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 01:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0052_remove_match_team_missed_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='hopper_load',
            field=models.CharField(max_length=999, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]