# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-06 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
    ]
