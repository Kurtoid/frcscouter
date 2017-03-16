# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0074_auto_20170314_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volley',
            name='match',
        ),
        migrations.DeleteModel(
            name='Volley',
        ),
    ]
