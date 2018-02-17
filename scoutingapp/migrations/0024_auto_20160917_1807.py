# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0023_auto_20160917_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endgamestate',
            name='state',
            field=models.CharField(max_length=20),
        ),
    ]
