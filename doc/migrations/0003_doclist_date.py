# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 15:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_auto_20160728_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='doclist',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
