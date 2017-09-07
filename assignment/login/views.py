from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import account

from .forms import NameForm, ContactForm, CreateAccount

# Create your views here.
##def loginPage(request):
##    if request.method == 'POST':
##        form = ContactForm(request.POST)
##        print(form.data['username'])
##        #data.save()
##    template = loader.get_template('login/login.html')
##    return render(request, 'login.html')

def loginPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateAccount(request.POST)
        # check whether it's valid:
        if form.is_valid():
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
                return render(request, 'login.html')
            else:
                messages.info(request, 'Passwords do no match')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateAccount()

    return render(request, 'name.html', {'form': form})
