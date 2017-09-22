# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from .models import User


def index(request):
    all_users = User.objects.all()
    template = loader.get_template('login/loginbase.html')

    context = {
        'all_users': all_users,
    }

    return HttpResponse(template.render(context, request))
