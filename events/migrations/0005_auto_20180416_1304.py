# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_events_going'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.TextField(),
        ),
    ]
