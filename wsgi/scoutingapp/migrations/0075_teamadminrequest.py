# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0074_auto_20170308_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamAdminRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fromUser', models.ForeignKey(related_name='fromuseradminrequest', to=settings.AUTH_USER_MODEL)),
                ('toTeam', models.ForeignKey(related_name='toteamadminrequest', to='scoutingapp.Team')),
            ],
        ),
    ]
