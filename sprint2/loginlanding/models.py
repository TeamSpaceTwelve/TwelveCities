# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class facilities(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    facilityType = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    description = models.TextField
    latitude = models.DecimalField(max_digits=8, decimal_places=4)
    longitude = models.DecimalField(max_digits=8, decimal_places=4)

    def __str__(self):
        return self.name


class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name + ' - ' + self.address


class Colleges(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name + ' - ' + self.address


class Libraries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name + ' - ' + self.address


class Industries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name + ' - ' + self.address
