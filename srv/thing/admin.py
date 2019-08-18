from django.contrib import admin
from .models import ThingType, Thing, Seat


admin.site.register(ThingType)
admin.site.register(Thing)
admin.site.register(Seat)
