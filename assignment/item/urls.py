from django.conf.urls import url

from . import views

app_name = 'item'
urlpatterns = [
    url(r'^$', views.itemList, name='itemList'),
    url('page/', views.itemPage, name='itemPage'),
]
