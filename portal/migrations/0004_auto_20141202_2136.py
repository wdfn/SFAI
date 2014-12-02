# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_event_deadline_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='description',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='student',
        ),
        migrations.AddField(
            model_name='submission',
            name='avatar_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='username',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
