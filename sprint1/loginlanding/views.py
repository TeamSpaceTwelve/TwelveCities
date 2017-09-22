from django.http import HttpResponse
from django.template import loader
from .models import Hotels, Libraries, Industries, Colleges


def index(request):
    all_hotels = Hotels.objects.all()
    all_libraries = Libraries.objects.all()
    all_colleges = Colleges.objects.all()
    all_industries = Industries.objects.all()
    template = loader.get_template('loginlanding/index.html')

    context = {
        'all_hotels': all_hotels,
        'all_libraries': all_libraries,
        'all_colleges': all_colleges,
        'all_industries': all_industries,
    }

    return HttpResponse(template.render(context, request))


def hoteldetail(request, specific_id):
    template = loader.get_template('loginlanding/detail.html')
    obj_details = Hotels.objects.filter(id=specific_id),
    context = {
        'obj_details': obj_details,
    }
    return HttpResponse(template.render(context, request))


