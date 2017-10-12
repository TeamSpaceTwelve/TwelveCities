from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.forms import formset_factory

from .models import account

from .forms import NameForm, ContactForm, CreateAccount, Login, UpdateAccount

def loginPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateAccount(request.POST)
        form2 = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if account.objects.filter(username = form2.data['username']).exists():
                messages.info(request, 'Username already taken.')
            else:
                if form2.data['password'] == form2.data['Retype']:
                    if form.data['password'] == form.data['Retype']:
                        data = account(username = form.data['username'],
                                       email = form.data['email'],
                                       password = form.data['password'],
                                       address = form.data['address'],
                                       type = form.data['Type'])
                        data.save()
                        # process the data in form.cleaned_data as required
                        # ...
                        # redirect to a new URL:
                        return redirect('/login/account/'+form.data['username'], permanent=True)
                else:
                    messages.info(request, 'Passwords do not match')
        elif form2.is_valid():
            if account.objects.filter(username = form2.data['username']).exists():
                print('yes')
                if form2.data['password'] == account.objects.values_list('password', flat=True).get(username = form2.data['username']):
                    print('logged in successfully')
                    return redirect('/login/account/'+form2.data['username'], permanent=True)
                else:
                    print('incorrect password')
                    #return redirect('/')
            else:
                print('username does not exist')
               # return redirect('/')
            return render(request, 'name.html')
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateAccount()
        form2 = Login()

    return render(request, 'name.html', {'form': form, 'form2': form2})

def accountPage(request, id):
    user = account.objects.get(username = id)
    if request.method == 'POST':
        form = UpdateAccount(request.POST)
        if form.is_valid():
            #data = user(email = form.data['email'],
             #              address = form.data['address'],
              #             type = form.data['Type'])
            user.email = form.data['email']
            user.address = form.data['address']
            user.type = form.data['Type']
            user.save()
    else:
        form = UpdateAccount(initial={'email': user.email,
                                      'address': user.address,
                                      'Type': user.type})
    return render(request, 'account.html', {'form': form, 'id':id})
#_to_response



##IM KEEPING THIS SH!T HERE JUST IN CASE
##

# Create your views here.
##def loginPage(request):
##    if request.method == 'POST':
##        form = ContactForm(request.POST)
##        print(form.data['username'])
##        #data.save()
##    template = loader.get_template('login/login.html')
##    return render(request, 'login.html')

##def loginPage(request):
##    if request.method == 'POST':
##        form = Login(request.POST)
##        if form.is_valid():
##                return render(request, 'login.html')
##    else:
##        form = Login()
##
##    return render(request, 'login2.html', {'form': form})
