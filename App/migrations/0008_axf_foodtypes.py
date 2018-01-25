# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_axf_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axf_foodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=100)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=100)),
                ('typesort', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
