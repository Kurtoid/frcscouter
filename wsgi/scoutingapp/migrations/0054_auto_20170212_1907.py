# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0053_auto_20170208_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volley',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hopper_load', models.CharField(max_length=999, null=True)),
                ('high_or_low', models.CharField(max_length=999, null=True)),
                ('high_efficiency_load', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='high_efficiency_load', to='scoutingapp.HighEfficiency')),
                ('low_efficiency_load', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='low_efficiency_load', to='scoutingapp.HighEfficiency')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='high_efficiency_load',
        ),
        migrations.RemoveField(
            model_name='match',
            name='hopper_load',
        ),
        migrations.RemoveField(
            model_name='match',
            name='low_efficiency_load',
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_high_efficiency_load',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auto_high_efficiency_load', to='scoutingapp.HighEfficiency'),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_hopper_load',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoutingapp.HopperLoad'),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_low_efficiency_load',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoutingapp.HighEfficiency'),
        ),
        migrations.AlterField(
            model_name='match',
            name='auto_trigger_hopper',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_aquired',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_picked_up',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='gears_scored',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='high_goals_missed',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='high_goals_scored',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='trigger_hopper',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True),
        ),
        migrations.AddField(
            model_name='volley',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ball_volley', to='scoutingapp.Match'),
        ),
    ]
