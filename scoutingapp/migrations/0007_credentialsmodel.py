# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import oauth2client.contrib.django_util.models


class Migration(migrations.Migration):

    dependencies = [
        ('scoutingapp', '0006_auto_20160806_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('credential', oauth2client.contrib.django_util.models.CredentialsField(null=True)),
            ],
        ),
    ]
