# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0059_auto_20170218_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='accuracy',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='ball_count',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='goal_type',
        ),
        migrations.AddField(
            model_name='gear',
            name='dropped',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gear',
            name='source',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
    ]
