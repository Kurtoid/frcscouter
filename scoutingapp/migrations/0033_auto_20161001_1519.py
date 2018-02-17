# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0032_auto_20160927_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='robot_1_end_game',
            new_name='robot_end_game',
        ),
    ]
