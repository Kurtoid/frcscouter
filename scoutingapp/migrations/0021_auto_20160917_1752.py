# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0020_auto_20160917_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliancematch',
            name='match_number',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='scouted_team',
            field=models.ForeignKey(default=1, to='scoutingapp.Team'),
            preserve_default=False,
        ),
    ]
