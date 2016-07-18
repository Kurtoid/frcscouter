"""
this module controls how URLs are handled in the Scoutingapp
"""
from django.conf.urls import url

from . import views
app_name = 'scoutingapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userlogin/$', views.userlogin, name='userlogin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^usercontrolpanel/$', views.usercontrolpanel,
        name='usercontrolpanel'),
    url(r'^logoutuser/$', views.logoutuser, name='logoutuser'),
    url(r'^scout/$', views.scout, name='scout'),
    url(r'^demoscout/$', views.demo_scout_page, name='demo_scout_page'),
    url(r'^fieldsetup/$', views.fieldsetupcontrol, name='fieldsetupcontrol'),
    url(r'^viewrounds/$', views.viewrounds, name='viewrounds'),
]
