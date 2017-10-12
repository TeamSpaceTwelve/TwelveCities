# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('username', models.CharField(max_length=200, primary_key='true', serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('0', 'Student'), ('1', 'Tourist'), ('2', 'Business'), ('3', 'Admin')], max_length=1)),
            ],
        ),
    ]