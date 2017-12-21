from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^editprofile/$', views.EditProfileView),
    url(r'^profile/$', views.ProfileView),
]