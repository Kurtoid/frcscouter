# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0082_auto_20170321_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='auto_hoppers_triggered',
            field=models.BooleanField(default=False),
        ),
    ]
