# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0060_auto_20170218_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='auto_gears_scored',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
