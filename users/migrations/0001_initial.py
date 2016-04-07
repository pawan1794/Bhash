# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-05 09:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserInfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]