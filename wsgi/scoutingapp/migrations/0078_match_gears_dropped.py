# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0077_auto_20170318_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='gears_dropped',
            field=models.DecimalField(max_digits=100, default=0, decimal_places=0),
            preserve_default=False,
        ),
    ]
