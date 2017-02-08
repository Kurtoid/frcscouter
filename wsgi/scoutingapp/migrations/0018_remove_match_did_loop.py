# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0017_match_did_loop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='did_loop',
        ),
    ]
