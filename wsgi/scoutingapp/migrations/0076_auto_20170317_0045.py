# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0075_auto_20170316_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='match',
        ),
        migrations.AddField(
            model_name='match',
            name='gears_type',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Gear',
        ),
    ]
