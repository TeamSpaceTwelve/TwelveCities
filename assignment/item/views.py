from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def itemList(request):
    return render(request, 'itemList.html', context=None)

def itemPage(request):
    return HttpResponse('a specific item will be here')
