# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0014_auto_20160917_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='fed_boulder',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=0),
        ),
    ]
