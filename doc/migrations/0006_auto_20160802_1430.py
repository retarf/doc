# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0005_auto_20160802_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Client'),
        ),
    ]