"""
this module controls how URLs are handled in the Scoutingapp
"""
from django.conf.urls import url

from . import views
app_name = 'scoutingapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userlogin/$', views.userlogin, name='userlogin'),
    url(r'^exporttogdocs/$', views.export_to_gdocs, name='export_to_gdocs'),
    url(r'^oauth2callback/$', views.auth_return, name='auth_return'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^usercontrolpanel/$', views.usercontrolpanel,
        name='usercontrolpanel'),
    url(r'^logoutuser/$', views.logoutuser, name='logoutuser'),
    url(r'^scout/$', views.scout, name='scout'),
    url(r'^demoscout/$', views.demo_scout_page, name='demo_scout_page'),
    url(r'^alliancescout/$', views.alliance_scout, name='alliance_scout'),
    url(r'^viewrounds/$', views.viewrounds, name='viewrounds'),
    url(r'^exportusers/$', views.exportusers, name='exportusers'),
    url(r'^importfromtba/$', views.import_from_TBA, name='import_from_TBA'),
    url(r'^importeventfromtba/$', views.import_event_from_TBA,
        name='import_event_from_TBA'),
    url(r'^exporthtml/(?P<team_number>[0-9]+)', views.exporthtml,
        name='exporthtml'),
    url(r'^allianceexporthtml/(?P<team_number>[0-9]+)', views.allianceexporthtml,
        name='allianceexporthtml')
]
