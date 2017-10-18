from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('(?P<specific_id>[0-9]+)/$', views.hoteldetail, name='hoteldetail'),
    url('in/(?P<id>[a-z,A-Z,0-9]+)/(?P<specific_id>[0-9]+)/$', views.hoteldetail, name='hoteldetail'),
    url('search/(?P<item>[a-z,A-Z,0-9]+)/$', views.results, name='results'),
    url('in/(?P<id>[a-z,A-Z,0-9]+)/$', views.index2, name='index'),
    url('(?P<id>[a-z,A-Z,0-9]+)/search/(?P<item>[a-z,A-Z,0-9]+)/$', views.results2, name='results'),
]
