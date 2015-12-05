from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from smarthome.api.models import *

class LightswitchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
		model = Lightswitch
		fields = ('id', 'name', 'on', 'level')

class LightsceneSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
		model = Lightscene
		fields = ('id', 'name', 'on')

class ThermostatSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
		model = Thermostat
		fields = ('id', 'name', 'tempset', 'tempactual', 'hold', 'heat')

class GarageopenerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
		model = Garageopener
		fields = ('id', 'name', 'open')
