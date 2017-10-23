from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.postgres import *
from .models import facilities, reviews
import login
from .forms import search, review
from itertools import chain
from login.models import UserProfile, User


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
    facility6 = facilities.objects.filter(facilityType__icontains='Park')
    facility3 = facilities.objects.filter(facilityType__icontains='Zoo')
    facility4 = facilities.objects.filter(facilityType__icontains='Museum')
    facility5 = facilities.objects.filter(facilityType__icontains='Mall')
    all_facilities = list(chain(facility1, facility2, facility3, facility4, facility5, facility6)
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

        facility1 = facilities.objects.filter(facilityType__icontains='Hotel')
        facility2 = facilities.objects.filter(facilityType__icontains='Park')
        facility3 = facilities.objects.filter(facilityType__icontains='Zoo')
        facility4 = facilities.objects.filter(facilityType__icontains='Museum')
        facility5 = facilities.objects.filter(facilityType__icontains='Mall')
        all_facilities = list(chain(facility1, facility2, facility3, facility4, facility5))
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
        facility6 = facilities.objects.filter(facilityType__icontains='Park')
        facility3 = facilities.objects.filter(facilityType__icontains='Zoo')
        facility4 = facilities.objects.filter(facilityType__icontains='Museum')
        facility5 = facilities.objects.filter(facilityType__icontains='Mall')
        all_facilities = list(chain(facility1, facility2, facility3, facility4, facility5, facility6))

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
    userReviews = reviews.objects.filter(facilityID=specific_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = review(request.POST)
            if form.is_valid():
                data = reviews(facilityID=specific_id,
                               review=form.data['review'],
                               score=form.data['score'],
                               user=request.user.id)
                data.save()
        else:
            form = review()
        print(details.address)
        return render(request, template, {'details': details, 'form': form, 'reviews': userReviews})
    else:
        print(details.address)
        return render(request, template, {'details': details, 'reviews': userReviews})


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



