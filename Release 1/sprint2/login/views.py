# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from .models import User
from .forms import UserForm, UserFormLogin, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import View
from django.contrib.auth.decorators import login_required


def index(request):
    all_users = User.objects.all()
    template = loader.get_template('login/loginbase.html')

    context = {
        'all_users': all_users,
    }

    return HttpResponse(template.render(context, request))


def logoutuser(request):
    logout(request)
    return redirect('/loginlanding')


class IndexLogin(View):
    form_class = UserFormLogin
    template = 'login/loginbase.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        #field is filled in
        password = form.data['password']
        username = form.data['username']
        user = authenticate(username=username, password=password)
        # if user exists
        if user is not None:
            login(request, user)
            return redirect('/loginlanding')
            # if login was unsuccessful then recreate login form
        return render(request, self.template, {'form': form})


class UserFormView(View):
    form_class = UserForm
    template_name = 'login/signup.html'

    #create login form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        #field is filled in
        if form.is_valid():
            #withhold data within form without pushing to database
            user = form.save(commit=False)
            #clean and format data
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            password = form.data['password']
            username = form.data['username']
            #set password with encryption
            user.set_password(password)
            #save user to database
            user.save()

            #login new user
            #user = authenticate(username=username, password=password)
            user = authenticate(username=username, password=password)
            #if user exists
            if user is not None:
                login(request, user)
                return redirect('/login/profile')
        #if login was unsuccessful then recreate login form
        return render(request, self.template_name, {'form': form})


@login_required
def user_profile(request):
    template_name = 'login/profile.html'
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/loginlanding')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    return render(request, template_name, {'form': form})
