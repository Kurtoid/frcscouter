# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='FieldSetup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('defense1', models.ForeignKey(to='scoutingapp.Defense', related_name='Defense_1')),
                ('defense2', models.ForeignKey(to='scoutingapp.Defense', related_name='Defense_2')),
                ('defense3', models.ForeignKey(to='scoutingapp.Defense', related_name='Defense_3')),
                ('defense4', models.ForeignKey(to='scoutingapp.Defense', related_name='Defense_4')),
                ('defense5', models.ForeignKey(to='scoutingapp.Defense', related_name='Defense_5')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('match_number', models.DecimalField(decimal_places=0, max_digits=100, default=0)),
                ('crossed_defense_on_auto', models.BooleanField(default=False)),
                ('auto_defense_crossed', models.DecimalField(decimal_places=0, max_digits=1, default=False)),
                ('auto_balls', models.DecimalField(decimal_places=0, max_digits=10, default=0)),
                ('high_balls', models.DecimalField(decimal_places=0, max_digits=10, default=0)),
                ('low_balls', models.DecimalField(decimal_places=0, max_digits=10, default=0)),
                ('score', models.DecimalField(decimal_places=0, max_digits=10, default=0)),
                ('did_loops', models.DecimalField(decimal_places=0, max_digits=100, default=0)),
                ('field_setup', models.OneToOneField(to='scoutingapp.FieldSetup')),
            ],
            options={
                'verbose_name_plural': 'Matches',
                'verbose_name': 'Match',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_number', models.DecimalField(primary_key=True, serialize=False, decimal_places=0, max_digits=5, default=0)),
                ('team_name', models.CharField(max_length=200, default='UNNAMED')),
            ],
            options={
                'ordering': ('team_number',),
                'verbose_name_plural': 'Teams',
                'verbose_name': 'Team',
            },
        ),
        migrations.AddField(
            model_name='myuser',
            name='team',
            field=models.ForeignKey(null=True, to='scoutingapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='scouted_by',
            field=models.ForeignKey(to='scoutingapp.MyUser'),
        ),
        migrations.AddField(
            model_name='match',
            name='scouted_team',
            field=models.ForeignKey(to='scoutingapp.Team'),
        ),
    ]
