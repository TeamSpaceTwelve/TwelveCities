# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hotels, Colleges, Libraries, Industries

admin.site.register(Hotels)
admin.site.register(Colleges)
admin.site.register(Libraries)
admin.site.register(Industries)
