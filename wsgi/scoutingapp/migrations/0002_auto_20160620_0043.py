# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, default='UNAMED')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='did_loops',
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(null=True, to='scoutingapp.Tournament'),
        ),
    ]
