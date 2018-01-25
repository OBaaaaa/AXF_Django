# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_axf_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axf_mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.CharField(max_length=200)),
                ('trackid', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
    ]