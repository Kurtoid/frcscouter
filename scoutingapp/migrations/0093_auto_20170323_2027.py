# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0092_auto_20170323_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='auto_gears_scored',
            field=models.ForeignKey(to='scoutingapp.GearAction', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='preloaded_gear_action',
            field=models.ForeignKey(to='scoutingapp.PreloadedGearAction', default=0, blank=True),
        ),
    ]
