# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0073_auto_20170302_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(default='', null=True, max_length=100),
        ),
    ]
