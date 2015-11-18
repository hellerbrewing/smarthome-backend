from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Lightswitch(models.Model):
    """
    This model represents a lightswitch.
    """
    name = models.CharField(max_length=20, blank=False, unique=True)
    on = models.BooleanField(default=False)
    level = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name

class Lightscene(models.Model):
    """
    This model represents a scene.
    """
    name = models.CharField(max_length=20, blank=False, unique=True)
    on = models.BooleanField(default=False)
    lightswitches = models.ManyToManyField(Lightswitch, related_name = "lightswitches")

class Thermostat(models.Model):
    """
    This model represents a thermostat.
    """
    name = models.CharField(max_length=20, blank=False, unique=True)
    tempset = models.IntegerField()
    tempactual = models.IntegerField()
    hold = models.BooleanField(default=False)
    heat = models.BooleanField(default=False)

class Garageopener(models.Model):
    """
    This model represents a garage door opener.
    """
    name = models.CharField(max_length=20, blank=False, unique=True)
    open = models.BooleanField(default=False)