# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0012_auto_20160917_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='low_bar_crossed',
            field=models.DecimalField(default=0, verbose_name='Low bar', decimal_places=0, max_digits=10),
        ),
    ]
