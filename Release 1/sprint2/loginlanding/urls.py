from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('item/(?P<specific_id>[0-9]+)/$', views.hoteldetail, name='hoteldetail'),
    url(r'^(?P<specific_id>[0-9]+)/$', views.hoteldetail, name='hoteldetail'),
    url('search/(?P<item>[a-z,A-Z,0-9]+)/$', views.results, name='results'),
    url(r'^student/$', views.landingstudent, name='student'),
    url(r'^tourist/$', views.landingtourist, name='tourist'),
    url(r'^business/$', views.landingbusiness, name='business'),
    url(r'^all/$', views.landingall, name='all'),
]