# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_description', models.CharField(max_length=1000)),
                ('exhibition_date', models.DateTimeField(verbose_name=b'exhibition date')),
                ('max_num_submissions', models.IntegerField(default=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
