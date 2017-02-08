# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0028_auto_20160917_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='alliancematch',
            name='robot_1_card',
            field=models.ForeignKey(to='scoutingapp.Card', related_name='Robot1card', null=True),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_2_card',
            field=models.ForeignKey(to='scoutingapp.Card', related_name='Robot2card', null=True),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_3_card',
            field=models.ForeignKey(to='scoutingapp.Card', related_name='Robot3card', null=True),
        ),
    ]
