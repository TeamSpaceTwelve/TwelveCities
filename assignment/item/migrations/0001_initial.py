# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('facilityType', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=8)),
            ],
        ),
    ]