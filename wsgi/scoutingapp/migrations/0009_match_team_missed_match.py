# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0008_auto_20160902_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='team_missed_match',
            field=models.BooleanField(default=False),
        ),
    ]
