# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0041_auto_20170204_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='auto_efficiency_load',
            field=models.DecimalField(choices=[(4, 'Great (75-95%)'), (1, 'Horrible (1-25%)'), (3, 'Good (50-75%)'), (5, 'Amazing (95-100%)'), (0, 'None (0)'), (2, 'Poor (25-50%)')], decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_hopper_load',
            field=models.DecimalField(choices=[(1, 'Small (10-25)'), (2, 'Medium (25-50)'), (3, 'Large (50-75)'), (5, 'Monster (100+)'), (4, 'Extra Large (75-100)'), (0, 'Start (10)')], decimal_places=0, default=0, max_digits=1),
        ),
        migrations.DeleteModel(
            name='HopperLoad',
        ),
    ]