# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Not Started'), (2, 'In Progress'), (3, 'Completed')], default=1),
        ),
    ]
