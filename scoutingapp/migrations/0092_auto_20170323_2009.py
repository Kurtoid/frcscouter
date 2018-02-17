# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0091_auto_20170323_2007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GearActions',
            new_name='GearAction',
        ),
    ]
