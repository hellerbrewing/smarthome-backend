from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from smarthome.api.models import *

class LightswitchSerializer(serializers.ModelSerializer):
    class Meta:
	model = Lightswitch
	fields = ('id', 'name', 'on', 'level')
class LightsceneSerializer(serializers.ModelSerializer):
    class Meta:
	model = Lightscene
	fields = ('id', 'name', 'on', 'lightswitches')
class ThermostatSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Thermostat
	fields = ('id', 'name', 'tempset', 'tempactual', 'hold', 'heat')
class GarageopenerSerializer(serializers.ModelSerializer):
    class Meta:
	model = Garageopener
	fields = ('id', 'name', 'open')
