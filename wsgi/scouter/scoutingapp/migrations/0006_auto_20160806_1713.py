# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0005_auto_20160718_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='auto_defense_crossed',
            field=models.ForeignKey(to='scoutingapp.Defense'),
        ),
    ]
