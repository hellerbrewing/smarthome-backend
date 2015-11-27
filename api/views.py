import pycurl
from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from smarthome.api.models import *

#REST API
from rest_framework import viewsets
from smarthome.api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse

def home (request):
	"""
	Send requests to / to the ember.js clientside app 
	"""

	return render_to_response('index.html', {}, RequestContext(request))

#needed if you want to use all class-based views, replace foo and bar with respective names (e.g. forumposts-list)
class APIRoot(APIView):
    def get(self, request):
        # Assuming we have views named 'foo-view' and 'bar-view'
        # in our project's URLconf.
        return Response({
            'lightswitches': reverse('lightswitch-list', request=request),
            'lightscenes': reverse('lightscene-list', request=request),
			'thermostats': reverse('thermostat-list', request=request),
			'garageopeners': reverse('garageopener-list', request=request),
		})

#Viewset forum post example
# class ForumpostViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows for CRUD operations on forumpost objects.
#     """
#     queryset = Forumpost.objects.all()
#     serializer_class = ForumpostSerializer

#more detailed, but more control class based view example

# Create your views here.
# I still need to get this working
class LightswitchList(APIView):
	"""
	List all lightswitches.
	"""
	def get (self, request, format=None):
		lightswitches = Lightswitch.objects.all()
		serializer = LightswitchSerializer(lightswitches, many=True, context={'request': request})
		return Response(serializer.data)

class LightswitchDetail(APIView):
	"""
	Retrieve, or upatae a single forum post.
	"""
	def get_object(self, pk):
		try:
			return Lightswitch.objects.get(pk=pk)
		except Lightswitch.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		lightswitch = self.get_object(pk)
		serializer = LightswitchSerializer(lightswitch, context={'request': request})
		return Response(serializer.data)

	def put (self, request, pk, format=None):
		lightswitch = self.get_object(pk)
		serializer = LightswitchSerializer(lightswitch, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			#insert PyCurl code here
			c = pycurl.Curl()
			u =('http://192.168.0.203/port_3480/data_request?id=lu_action&output_format=json&DeviceNum=%s&serviceId=urn:upnp-org:serviceId:Dimming1&action=SetLoadLevelTarget&newLoadlevelTarget=%s' % (lightswitch.deviceID, lightswitch.level))
			#l = lightswitch.level
			print u
			c.setopt(c.URL, u)
			c.perform()
			#debugging code
			print u
			print lightswitch.level
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LightsceneList(APIView):
	"""
	List all scenes.
	"""
	def get (self, request, format=None):
		lightscenes = Lightscene.obects.all()
		serializer = LightsceneSerializer(lightscenes, many=True, context={'request': request})
		return Response(serializer.data)

class LightsceneDetail(APIView):
	"""
	Retrieve, or update a single scene.
	"""
	def get_object(self, pk):
		try:
			return Lightscene.objects.get(pk=pk)
		except Lightscene.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		lightscene = self.get.object(pk)
		serializer = LightsceneSerializer(lightscene, context={'request': request})
		return Response(serializer.data)

	def put (self, request, pk, format=None):
		lightscene = self.get_object(pk)
		serializer = LightsceneSerializer(lightscene, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			#insert curl command here
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThermostatList(APIView):
	"""
	List all thermostats.
	"""
	def get (self, request, format=None):
		thermostats = Thermostats.objects.all()
		serializer = ThermostatSerializer(thermostats, many=True, context={'request': request})
		return Response(serializer.data)

class ThermostatDetail(APIView):
	"""
	Retrieve or update a single thermostat.
	"""
	def get_object(self, pk):
		try:
			return Thermostat.objects.get(pk=pk)
		except Thermostat.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		thermostat = self.get.object(pk)
		serializer = ThermostatSerializer(thermostat, context={'request': request})
		return Response(serializer.data)

	def put (self, request, pk, format=None):
		thermostat = self.get_object(pk)
		serializer = ThermostatSerializer(thermostat, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			#insert curl command here
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GarageopenerList(APIView):
	"""
	List all garage door openers.
	"""
	def get (self, request, format=None):
		garageopener = Garageopener.objects.all()
		serializer = GarageopenerSerializer(garageopener, many=True, context={'request': request})
		return Response(serializer.data)

class GarageopenerDetail(APIView):
	"""
	Retrieve or update a single garage door opener.
	"""
	def get_object(self, pk):
		try:
			return Garageopener.objects.get(pk=pk)
		except Garageopener.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		garageopener = self.get.object(pk)
		serializer = GarageopenerSerializer(thermostat, context={'request': request})
		return Response(serializer.data)

	def put (self, request, pk, format=None):
		garageopener = self.get_object(pk)
		serializer = GarageopenerSerializer(garageopener, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			#insert curl command here
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)