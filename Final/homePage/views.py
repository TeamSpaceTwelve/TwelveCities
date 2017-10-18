# Create your views here.
# homePage/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'homePage.html', context=None)

def loggedIn(request, id):
    return render(request, 'homePage_loggedIn.html', {'id': id})