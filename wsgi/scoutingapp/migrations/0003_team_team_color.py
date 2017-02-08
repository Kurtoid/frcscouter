# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0002_auto_20160620_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_color',
            field=models.CharField(null=True, max_length=7),
        ),
    ]
