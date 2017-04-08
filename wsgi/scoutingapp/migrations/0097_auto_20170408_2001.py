# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0096_auto_20170408_2000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preloadedgearaction',
            options={'ordering': ['updated_at']},
        ),
    ]
