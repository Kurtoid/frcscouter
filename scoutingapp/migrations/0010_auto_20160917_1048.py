# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0009_match_team_missed_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='auto_balls',
        ),
        migrations.AddField(
            model_name='match',
            name='auto_high_balls',
            field=models.DecimalField(max_digits=10, default=0, decimal_places=0),
        ),
        migrations.AddField(
            model_name='match',
            name='auto_low_balls',
            field=models.DecimalField(max_digits=10, default=0, decimal_places=0),
        ),
    ]
