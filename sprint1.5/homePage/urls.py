# homePage/urls.py
from django.conf.urls import url
from homePage import views

urlpatterns = [
   url(r'^home/$', views.HomePageView.as_view()),
   url('home/(?P<id>[a-z A-Z 0-9]+)/$', views.loggedIn, name='loggedIn')
]
