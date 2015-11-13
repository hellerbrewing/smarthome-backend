from django.contrib import admin
from smarthome.api.models import *

# Register your models here.

admin.site.register(Lightswitch)
admin.site.register(Lightscene)
admin.site.register(Thermostat)
admin.site.register(Garageopener)

