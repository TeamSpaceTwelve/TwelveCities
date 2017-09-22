# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250, editable=False)

    def __str__(self):
        return self.username
