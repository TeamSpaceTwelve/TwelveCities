from django.http import HttpResponse
from django.template import loader
from .models import facilities


def index(request):
    all_facilities = facilities.objects.all()
    template = loader.get_template('loginlanding/index.html')

    context = {
        'all_facilities': all_facilities,
    }

    return HttpResponse(template.render(context, request))


def hoteldetail(request, specific_id):
    template = loader.get_template('loginlanding/detail.html')
    obj_details = facilities.objects.filter(id=specific_id),
    context = {
        'obj_details': obj_details,
    }
    return HttpResponse(template.render(context, request))


