# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0036_auto_20161001_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldsetup',
            name='defense1',
        ),
    ]
