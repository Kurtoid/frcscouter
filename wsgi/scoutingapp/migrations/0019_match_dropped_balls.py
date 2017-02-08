# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0018_remove_match_did_loop'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='dropped_balls',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
