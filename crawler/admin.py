from django.contrib import admin
from .models import *
# Register your models here.

class Maliciousurls(admin.ModelAdmin):
    list_display = ['equip_id', 'domain']

class maliciouswebsites(admin.ModelAdmin):
    list_display = ['equip_id', 'domain']

admin.site.register(MaliciousUrls, Maliciousurls)
admin.site.register(MaliciousWebsites, maliciouswebsites)

