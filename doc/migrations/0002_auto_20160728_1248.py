# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='number',
            field=models.IntegerField(),
        ),
    ]