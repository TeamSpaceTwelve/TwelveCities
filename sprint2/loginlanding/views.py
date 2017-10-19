from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.postgres import *
from .models import facilities
from .forms import search
from itertools import chain
from login.models import UserProfile


def index(request):
    if request.user.is_authenticated:

        if request.user.profile.role == '0':
            return redirect('/loginlanding/student')

        elif request.user.profile.role == '1':
            return redirect('/loginlanding/tourist')

        elif request.user.profile.role == '2':
            return redirect('/loginlanding/business')
        else:
            return redirect('/loginlanding/all')

    else:
        if request.method == 'POST':
            form = search(request.POST)
            if form.is_valid():
                userSearch = form.data['search']
                return redirect('/loginlanding/search/' + userSearch, permanent=True)
        else:
            form = search()

        all_facilities = facilities.objects.all()
        template = loader.get_template('loginlanding/index.html')

        context = {
            'all_facilities': all_facilities,
        }

        # return HttpResponse(template.render(context, request), {'form':form})
        return render(request, 'loginlanding/index.html', {'all_facilities': all_facilities, 'form': form})


def landingstudent(request):
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/loginlanding/search/' + userSearch, permanent=True)
    else:
        form = search()

    facility1 = facilities.objects.filter(facilityType__icontains='Library')
    facility2 = facilities.objects.filter(facilityType__icontains='University')
    all_facilities = list(chain(facility1, facility2)
                          )
    template = loader.get_template('loginlanding/index.html')

    context = {
        'all_facilities': all_facilities,
    }

    # return HttpResponse(template.render(context, request), {'form':form})
    return render(request, 'loginlanding/index.html', {'all_facilities': all_facilities, 'form': form})


def landingtourist(request):
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/loginlanding/search/' + userSearch, permanent=True)
    else:
        form = search()

        all_facilities = facilities.objects.filter(facilityType__icontains='Hotel')
    template = loader.get_template('loginlanding/index.html')

    context = {
        'all_facilities': all_facilities,
    }

    # return HttpResponse(template.render(context, request), {'form':form})
    return render(request, 'loginlanding/index.html', {'all_facilities': all_facilities, 'form': form})


def landingbusiness(request):
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/loginlanding/search/' + userSearch, permanent=True)
    else:
        form = search()

        facility1 = facilities.objects.filter(facilityType__icontains='Hotel')
        facility2 = facilities.objects.filter(facilityType__icontains='Industry')
        all_facilities = list(chain(facility1, facility2))

    template = loader.get_template('loginlanding/index.html')

    context = {
        'all_facilities': all_facilities,
    }

    # return HttpResponse(template.render(context, request), {'form':form})
    return render(request, 'loginlanding/index.html', {'all_facilities': all_facilities, 'form': form})

def landingall(request):
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('/loginlanding/search/' + userSearch, permanent=True)
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
    template = 'loginlanding/detail.html'
    details = facilities.objects.get(id=specific_id)
    print(details.address)
    return render(request, template, {'details': details})


def results(request, item):
    all_facilities = facilities.objects.filter(name__icontains=item)
    print(all_facilities)
    print(item)
    #all_facilities = facilities.objects.all()
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            userSearch = form.data['search']
            return redirect('loginlanding/search/'+userSearch, permanent=True)
    else:
        form = search()
    return render(request, 'loginlanding/search.html', {'all_facilities': all_facilities, 'form': form})



