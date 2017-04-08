# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0094_auto_20170323_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliancematch',
            name='auto_pilot_gears_acquired',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)], default=0, decimal_places=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='auto_pilot_rotors_engaged',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)], default=0, decimal_places=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_gears_acquired',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(14), django.core.validators.MinValueValidator(0)], default=0, decimal_places=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='alliancematch',
            name='pilot_rotors_engaged',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], default=0, decimal_places=0, max_digits=1),
        ),
    ]
