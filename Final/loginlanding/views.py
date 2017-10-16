from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.postgres import *
from .models import facilities
from .forms import search

import operator
from django.db.models import Q


def index(request):
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/item/search/'+userSearch, permanent=True)
    else:
        form = search()
        
    all_facilities = facilities.objects.all()
    template = loader.get_template('loginlanding/index.html')

    context = {
        'all_facilities': all_facilities,
    }

    #return HttpResponse(template.render(context, request), {'form':form})
    return render(request, 'loginlanding/index.html', {'all_facilities': all_facilities, 'form': form})


def index2(request, id):
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/item/' + id + '/search/' + userSearch, permanent=True)
    else:
        form = search()

    all_facilities = facilities.objects.all()
    template = loader.get_template('loginlanding/index.html')

    context = {
        'all_facilities': all_facilities,
    }

    # return HttpResponse(template.render(context, request), {'form':form})
    return render(request, 'loginlanding/index.html', {'all_facilities': all_facilities, 'form': form})


def hoteldetail(request, specific_id):
    template = loader.get_template('loginlanding/detail.html')
    obj_details = facilities.objects.filter(id=specific_id),
    context = {
        'obj_details': obj_details,
    }
    return HttpResponse(template.render(context, request))

def results(request, item):
    all_facilities = facilities.objects.filter(name__icontains=item)
    print(all_facilities)
    print(item)
    #all_facilities = facilities.objects.all()
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/item/search/'+userSearch, permanent=True)
    else:
        form = search()
    return render(request, 'loginlanding/search.html', {'all_facilities': all_facilities, 'form': form})

def results2(request, item, id):
    all_facilities = facilities.objects.filter(name__icontains=item)
    print(all_facilities)
    print(item)
    #all_facilities = facilities.objects.all()
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/item/' + id + 'search/'+userSearch, permanent=True)
    else:
        form = search()
    return render(request, 'loginlanding/search.html', {'all_facilities': all_facilities, 'form': form})

