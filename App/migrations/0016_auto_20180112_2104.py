# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_auto_20180112_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.Order'),
        ),
    ]
