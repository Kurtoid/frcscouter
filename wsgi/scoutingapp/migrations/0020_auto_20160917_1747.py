# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0019_match_dropped_balls'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AllianceMatch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('alliance', models.ForeignKey(to='scoutingapp.Alliance')),
                ('field_setup', models.OneToOneField(to='scoutingapp.FieldSetup')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='field_setup',
        ),
    ]
