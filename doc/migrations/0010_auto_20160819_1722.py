# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0009_auto_20160819_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='value',
            field=models.FloatField(blank=True),
        ),
    ]