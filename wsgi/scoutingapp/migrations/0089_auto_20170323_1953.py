# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0088_auto_20170323_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreloadedGearAction',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_type',
            field=models.CharField(max_length=100, verbose_name='Gear Source', null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='preloaded_gear_action',
            field=models.ForeignKey(to='scoutingapp.PreloadedGearAction', default=0),
            preserve_default=False,
        ),
    ]
