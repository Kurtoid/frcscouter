# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0084_auto_20170321_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='robot_card',
            field=models.ForeignKey(related_name='Robot1card', blank=True, to='scoutingapp.Card', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
