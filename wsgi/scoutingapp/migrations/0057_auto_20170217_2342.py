# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0056_auto_20170215_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='auto_move_yn',
            field=models.BooleanField(verbose_name='Moved on auto?', default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_score_gear_yn',
            field=models.BooleanField(verbose_name='Did it score on auto?', default=False),
        ),
    ]
