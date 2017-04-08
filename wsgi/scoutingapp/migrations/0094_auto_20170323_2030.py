# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0093_auto_20170323_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='preloaded_gear_action',
            field=models.ForeignKey(default=0, null=True, to='scoutingapp.PreloadedGearAction', blank=True),
        ),
    ]
