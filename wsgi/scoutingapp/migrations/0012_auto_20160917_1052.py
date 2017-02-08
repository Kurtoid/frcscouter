# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0011_auto_20160917_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='defense1_crossed',
            new_name='low_bar_crossed',
        ),
        migrations.AddField(
            model_name='match',
            name='auto_dropped_ball',
            field=models.BooleanField(default=False),
        ),
    ]
