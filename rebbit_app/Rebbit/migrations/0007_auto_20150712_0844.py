# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rebbit', '0006_auto_20150712_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
    ]
