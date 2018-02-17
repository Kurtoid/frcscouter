# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0013_auto_20160917_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='crossed_defense_on_auto',
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_defense_crossed',
            field=models.ForeignKey(null=True, to='scoutingapp.Defense'),
        ),
    ]
