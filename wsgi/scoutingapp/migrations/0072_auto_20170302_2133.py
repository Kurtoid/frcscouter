# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0071_auto_20170302_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliancematch',
            name='auto_pilot_1_gears_acquired',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='auto_pilot_1_rotors_engaged',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='auto_pilot_2_gears_acquired',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='auto_pilot_2_rotors_engaged',
            field=models.DecimalField(max_digits=1, decimal_places=0, default=0),
        ),
    ]
