# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0010_auto_20160917_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='auto_high_balls',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_low_balls',
            field=models.BooleanField(default=False),
        ),
    ]
