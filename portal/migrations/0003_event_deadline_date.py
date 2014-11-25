# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20141125_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='deadline_date',
            field=models.DateTimeField(default=datetime.date(2014, 11, 25), verbose_name=b'deadline date'),
            preserve_default=False,
        ),
    ]
