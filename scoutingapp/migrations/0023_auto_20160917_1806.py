# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0022_alliancematch_scouted_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndGameState',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='alliancematch',
            name='scouted_team',
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_1_breach_ability',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_1_driver_skill',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_2_breach_ability',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_2_driver_skill',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_3_breach_ability',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='alliancematch',
            name='robot_3_driver_skill',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=10),
        ),
    ]
