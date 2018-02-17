# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0058_auto_20170218_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('goal_type', models.CharField(max_length=100)),
                ('accuracy', models.CharField(max_length=100)),
                ('ball_count', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='gears_aquired',
            field=models.DecimalField(decimal_places=0, null=True, max_digits=1, default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='gears_picked_up',
            field=models.DecimalField(decimal_places=0, null=True, max_digits=1, default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='gears_scored',
            field=models.DecimalField(decimal_places=0, null=True, max_digits=1, default=0),
        ),
        migrations.AddField(
            model_name='gear',
            name='match',
            field=models.ForeignKey(to='scoutingapp.Match'),
        ),
    ]
