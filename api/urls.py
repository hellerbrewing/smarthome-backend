from django.conf.urls import include, url

# Django Rest Framework
from rest_framework import routers
from localsettings import *
if isDev == True:
    from smarthome.api import views
else:
    from api import views
from rest_framework.urlpatterns import format_suffix_patterns

#REST API routes
router = routers.DefaultRouter()

#REST API
urlpatterns = [
	#url(r'^', include(router.urls)),
	url(r'^$', views.APIRoot.as_view(), name='api-root'),
	url(r'^lightswitches/$', views.LightswitchList.as_view(), name='lightswitch-list'),
	url(r'^lightswitches/(?P<pk>[0-9]+)/$', views.LightswitchDetail.as_view(), name='lightswitch-detail'),
	url(r'^lightscenes/$', views.LightsceneList.as_view(), name='lightscene-list'),
	url(r'^lightscenes/(?P<pk>[0-9]+)/$', views.LightsceneDetail.as_view(), name='lightscene-detail'),
	url(r'^thermostats/$', views.ThermostatList.as_view(), name='thermostat-list'),
	url(r'^thermostats/(?P<pk>[0-9]+)/$', views.ThermostatDetail.as_view(), name='thermostat-detail'),
	url(r'^garageopeners/$', views.GarageopenerList.as_view(), name='garageopener-list'),
	url(r'^garageopeners/(?P<pk>[0-9]+)/$', views.GarageopenerDetail.as_view(), name='garageopener-detail'),
	url(r'^session/', views.Session.as_view()),
]