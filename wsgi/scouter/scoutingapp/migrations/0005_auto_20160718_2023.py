# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0004_auto_20160706_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldsetup',
            name='defense1',
            field=models.ForeignKey(related_name='Defense_1', to='scoutingapp.Defense', verbose_name='Defense 1'),
        ),
        migrations.AlterField(
            model_name='fieldsetup',
            name='defense2',
            field=models.ForeignKey(related_name='Defense_2', to='scoutingapp.Defense', verbose_name='Defense 2'),
        ),
        migrations.AlterField(
            model_name='fieldsetup',
            name='defense3',
            field=models.ForeignKey(related_name='Defense_3', to='scoutingapp.Defense', verbose_name='Defense 3'),
        ),
        migrations.AlterField(
            model_name='fieldsetup',
            name='defense4',
            field=models.ForeignKey(related_name='Defense_4', to='scoutingapp.Defense', verbose_name='Defense 4'),
        ),
        migrations.AlterField(
            model_name='fieldsetup',
            name='defense5',
            field=models.ForeignKey(related_name='Defense_5', to='scoutingapp.Defense', verbose_name='Defense 5'),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_balls',
            field=models.DecimalField(verbose_name='Auto - Balls Made', max_digits=10, default=0, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_defense_crossed',
            field=models.DecimalField(verbose_name='Auto - Defense Crossed', max_digits=1, default=False, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='defense1_crossed',
            field=models.DecimalField(verbose_name='Defense 1', max_digits=10, default=0, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='defense2_crossed',
            field=models.DecimalField(verbose_name='Defense 2', max_digits=10, default=0, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='defense3_crossed',
            field=models.DecimalField(verbose_name='Defense 3', max_digits=10, default=0, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='defense4_crossed',
            field=models.DecimalField(verbose_name='Defense 4', max_digits=10, default=0, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='defense5_crossed',
            field=models.DecimalField(verbose_name='Defense 5', max_digits=10, default=0, decimal_places=0),
        ),
    ]
