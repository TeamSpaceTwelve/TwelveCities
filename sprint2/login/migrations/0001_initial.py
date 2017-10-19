# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(editable=False, max_length=250)),
                ('role', models.CharField(choices=[('0', 'Student'), ('1', 'Tourist'), ('2', 'Business'), ('3', 'Admin')], max_length=1)),
            ],
        ),
    ]
