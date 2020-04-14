from django.contrib import admin

from .models import stockAPIData, resourcesData


admin.site.register(stockAPIData)
admin.site.register(resourcesData)