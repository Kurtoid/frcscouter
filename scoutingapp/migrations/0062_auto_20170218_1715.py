# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0061_match_auto_gears_scored'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='gears_aquired',
        ),
        migrations.RemoveField(
            model_name='match',
            name='gears_picked_up',
        ),
        migrations.RemoveField(
            model_name='match',
            name='gears_scored',
        ),
    ]
