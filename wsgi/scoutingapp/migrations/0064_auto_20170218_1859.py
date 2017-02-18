# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0063_auto_20170218_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='auto_low_goal',
        ),
        migrations.AddField(
            model_name='match',
            name='auto_low_efficiency_load',
            field=models.ForeignKey(to='scoutingapp.HighEfficiency', null=True),
        ),
    ]
