# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20171220_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('plate_number', models.CharField(default=' ', max_length=50, primary_key=True, serialize=False, verbose_name='plate_number')),
                ('point', models.TextField(default=' ', verbose_name='point')),
                ('point_time', models.TextField(default=' ', verbose_name='point_time')),
            ],
        ),
        migrations.DeleteModel(
            name='village',
        ),
    ]
