# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0073_auto_20170302_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('event', models.ForeignKey(to='scoutingapp.Tournament')),
                ('teams', models.ManyToManyField(related_name='collaborationTeamRel', to='scoutingapp.Team')),
            ],
        ),
        migrations.CreateModel(
            name='CollaborationRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('fromTeam', models.ForeignKey(to='scoutingapp.Team', related_name='fromteamcollabrequest')),
                ('toTeam', models.ForeignKey(to='scoutingapp.Team', related_name='toteamcollabrequest')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='team_admins',
            field=models.ManyToManyField(related_name='teamAdminRel', to='scoutingapp.Team'),
        ),
    ]
