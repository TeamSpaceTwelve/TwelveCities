from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.loginPage, name='loginPage'),
    url('account/(?P<id>[a-z A-Z 0-9]+)/$', views.accountPage, name='accountPage'),
]
