# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0068_auto_20170219_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='duplicate',
            field=models.DecimalField(decimal_places=0, max_digits=100, null=True),
        ),
    ]
