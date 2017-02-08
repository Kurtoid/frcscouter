# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0037_remove_fieldsetup_defense1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='auto_defense_crossed',
            field=models.ForeignKey(null=True, to='scoutingapp.Defense', blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(null=True, to='scoutingapp.Tournament', blank=True),
        ),
    ]
