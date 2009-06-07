from django.contrib import admin
from models import City, Location

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'city', 'display_in_list',)
    list_display_links = ('name',) 
    list_editable = ('display_in_list',) 
    list_filter = ('city','display_in_list',) 

admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
