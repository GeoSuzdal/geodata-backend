from django.contrib import admin

from .models import Records, GeojsonObjects

admin.site.register(Records)
admin.site.register(GeojsonObjects)

