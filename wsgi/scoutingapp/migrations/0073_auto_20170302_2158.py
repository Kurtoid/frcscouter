# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0072_auto_20170302_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_1_team',
            field=models.ForeignKey(default=1, to='scoutingapp.Team', related_name='p1team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='pilot_2_team',
            field=models.ForeignKey(default=1, to='scoutingapp.Team', related_name='p2team'),
            preserve_default=False,
        ),
    ]
