# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0016_match_high_balls_missed'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='did_loop',
            field=models.BooleanField(default=False),
        ),
    ]
