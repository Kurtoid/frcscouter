# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0066_auto_20170218_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='per_match_id',
        ),
    ]
