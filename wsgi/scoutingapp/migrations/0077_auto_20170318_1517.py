# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0076_auto_20170317_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='gears_scored',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_type',
            field=models.CharField(max_length=100, default=0),
            preserve_default=False,
        ),
    ]
