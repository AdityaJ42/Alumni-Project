# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_in', '0003_auto_20180415_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(upload_to='profile pics/'),
        ),
    ]
