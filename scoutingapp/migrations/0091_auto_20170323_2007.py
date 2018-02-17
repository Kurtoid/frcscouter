# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0090_auto_20170323_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='GearActions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_gears_scored',
            field=models.ForeignKey(to='scoutingapp.GearActions'),
        ),
    ]
