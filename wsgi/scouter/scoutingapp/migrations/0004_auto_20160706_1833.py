# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0003_team_team_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='defense1_crossed',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='match',
            name='defense2_crossed',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='match',
            name='defense3_crossed',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='match',
            name='defense4_crossed',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='match',
            name='defense5_crossed',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
    ]
