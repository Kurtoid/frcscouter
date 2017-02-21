# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0067_remove_gear_per_match_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='duplicate',
            field=models.DecimalField(max_digits=100, decimal_places=0, null=True),
        ),
        migrations.AddField(
            model_name='volley',
            name='duplicate',
            field=models.DecimalField(max_digits=100, decimal_places=0, null=True),
        ),
    ]
