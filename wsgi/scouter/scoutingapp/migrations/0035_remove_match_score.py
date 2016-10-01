# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0034_auto_20161001_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='score',
        ),
    ]
