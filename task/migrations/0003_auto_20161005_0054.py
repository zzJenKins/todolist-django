# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-05 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20160913_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]