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
from rest_framework.responses import Response
from rest_framework import status

#needed if you want to use all class-based views, replace foo and bar with respective names (e.g. forumposts-list)
# class APIRoot(APIView):
#     def get(self, request):
#         # Assuming we have views named 'foo-view' and 'bar-view'
#         # in our project's URLconf.
#         return Response({
#             'foo': reverse('foo-view', request=request),
#             'bar': reverse('bar-view', request=request)
#         })

#Viewset forum post example
# class ForumpostViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows for CRUD operations on forumpost objects.
#     """
#     queryset = Forumpost.objects.all()
#     serializer_class = ForumpostSerializer

#more detailed, but more control class based view example

# Create your views here.
