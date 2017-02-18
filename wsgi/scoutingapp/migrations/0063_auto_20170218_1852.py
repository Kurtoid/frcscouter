# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0062_auto_20170218_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='auto_low_efficiency_load',
        ),
        migrations.RemoveField(
            model_name='match',
            name='auto_score_gear_yn',
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_move_yn',
            field=models.BooleanField(verbose_name='Auto Move', default=False),
        ),
    ]
