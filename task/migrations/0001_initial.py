# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-11 17:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, '未开始'), (1, '已完成')])),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
