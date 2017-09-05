from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def loginPage(request):
    template = loader.get_template('login/login.html')
    return render(request, 'login.html', context=None)
