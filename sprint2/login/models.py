# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

roles = (
    ('0', 'Student'),
    ('1', 'Tourist'),
    ('2', 'Business'),
)


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=250)
#     password = models.CharField(max_length=250, editable=False)
#     role = models.CharField(max_length=1, choices=roles)
#
#     def __str__(self):
#         return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=1, choices=roles)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
