# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0080_auto_20170321_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='currently_in_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='scoutingapp.Tournament', null=True),
        ),
    ]
