from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexLogin.as_view(), name='login'),
    url(r'^signup', views.UserFormView.as_view(), name='signup'),
    url(r'^logout', views.logoutuser, name='logout'),
    url(r'^profile/$', views.user_profile, name='profile'),
]