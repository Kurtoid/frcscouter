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
    url(r'^exporthtml/(?P<event_code>[a-zA-Z0-9]+)', views.exporthtml,
        name='exporthtml'),
    url(r'^exportteam/$', views.exportteam,
        name='exportteam'),
    url(r'^allianceexporthtml/(?P<event_code>[a-zA-Z0-9]+)', views.allianceexporthtml,
        name='allianceexporthtml'),
    url(r'^gethoppertypes/$', views.gethoppertypes, name='hoppertypes'),
    url(r'^getshottypes/$', views.getshottypes, name='getshottypes'),
    url(r'^getveff/$', views.getveff, name='getveff'),
    url(r'^getgearsource/$', views.gearsource, name='gearsource'),
    url(r'^getgeardropped/$', views.geardropped, name='geardropped'),
    # url(r'^getcategories/$', views.getcategories, name='getcategories'),
    url(r'^openhouse/$', views.openhousepage, name='openhouse'),

    url(r'^api/teambyevent/(?P<event_code>[a-zA-Z0-9]+)/(?P<match_id>[0-9]+)', views.api_teambyevent,
        name = 'api_teambyevent')

]
