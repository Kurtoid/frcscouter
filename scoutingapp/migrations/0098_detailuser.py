# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0097_auto_20170408_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(null=True, default='', max_length=100)),
                ('last_name', models.CharField(null=True, default='', max_length=100)),
                ('email', models.EmailField(max_length=255, verbose_name='email address', unique=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
