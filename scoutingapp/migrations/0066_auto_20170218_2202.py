# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0065_volley_per_match_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volley',
            name='per_match_id',
        ),
        migrations.AddField(
            model_name='gear',
            name='per_match_id',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=100),
            preserve_default=False,
        ),
    ]
