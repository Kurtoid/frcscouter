# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0087_auto_20170323_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliancematch',
            name='fails_to_spin_rotors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='forgot_reserve_gear',
            field=models.BooleanField(default=False),
        ),
    ]
