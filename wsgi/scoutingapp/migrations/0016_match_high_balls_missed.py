# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0015_match_fed_boulder'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='high_balls_missed',
            field=models.DecimalField(decimal_places=0, max_digits=10, default=0),
        ),
    ]
