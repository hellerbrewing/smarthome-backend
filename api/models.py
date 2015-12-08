from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from localsettings import *
if isDev == True:
    from smarthome.api.validators import *
else:
    from api.validators import *

# Create your models here.
class Lightswitch(models.Model):
    """
    This model represents a lightswitch.
    """
    name = models.CharField(max_length=20, blank=False, unique=True, validators=[removeJavascriptKeyword])
    deviceID = models.IntegerField(blank=True, null=True)
    on = models.BooleanField(default=False)
    level = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Lightscene(models.Model):
    """
    This model represents a scene.
    """
    name = models.CharField(max_length=20, blank=False, unique=True, validators=[removeJavascriptKeyword])
    on = models.BooleanField(default=False)
    sceneID = models.IntegerField(blank=True, null=True)
    #lightswitches = models.ManyToManyField(Lightswitch, related_name = "lightswitches")

    def __unicode__(self):
        return self.name

class Thermostat(models.Model):
    """
    This model represents a thermostat.
    """
    name = models.CharField(max_length=20, blank=False, unique=True, validators=[removeJavascriptKeyword])
    tempset = models.IntegerField()
    tempactual = models.IntegerField()
    hold = models.BooleanField(default=False)
    heat = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Garageopener(models.Model):
    """
    This model represents a garage door opener.
    """
    name = models.CharField(max_length=20, blank=False, unique=True, validators=[removeJavascriptKeyword])
    open = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
