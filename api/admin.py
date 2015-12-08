from django.contrib import admin
from localsettings import *
if isDev == True:
	from smarthome.api.models import *
else:
	from api.models import *

# Register your models here.

admin.site.register(Lightswitch)
admin.site.register(Lightscene)
admin.site.register(Thermostat)
admin.site.register(Garageopener)

