from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('(?P<specific_id>[0-9]+)/$', views.hoteldetail, name='hoteldetail')
]
