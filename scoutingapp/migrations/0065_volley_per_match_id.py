# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0064_auto_20170218_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='volley',
            name='per_match_id',
            field=models.DecimalField(decimal_places=0, max_digits=100, default=1),
            preserve_default=False,
        ),
    ]
