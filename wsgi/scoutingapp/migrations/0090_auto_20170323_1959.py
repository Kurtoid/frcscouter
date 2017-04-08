# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0089_auto_20170323_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='preloaded_gear_action',
            field=models.ForeignKey(to='scoutingapp.PreloadedGearAction', default=0),
        ),
    ]
