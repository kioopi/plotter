from django.contrib import admin
from models import Category, Termin, RecurringTermin

class TerminAdmin(admin.ModelAdmin):
    list_display = ('summary','startdate', 'publish', '_rule_description')
    list_display_links = ('summary', 'startdate') 
    list_editable = ('publish',) 
    list_filter = ('startdate', 'publish')
    search_fields = ('slug', 'summary', 'description')
    date_hierarchy = 'startdate'
    prepopulated_fields = {'slug': ('summary',)}
    fieldsets = (
      (None, {'fields': ('startdate','starttime','enddate','summary','slug',)}),
      (None, {'fields': ('description', 'organizers', 'location')}),
      (None, {'fields': ('publish', 'categories',)}),
    )

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RecurringTerminAdmin(admin.ModelAdmin):
    list_display = ('name','rule_description' )
    search_fields = ('name', 'summary', 'description')
    fieldsets = (
      (None, {'fields':('name','rule_description', 'weekday')}),
      ('Rule', {'fields':('frequency', 'first_date', 'interval', 'byweekday')}),
      ('Creation', {'fields':('createdelta',)}),
      (None, {'fields': ('starttime', 'duration', 'summary',)}),
      (None, {'fields': ('description', 'organizers', 'location')}),
      (None, {'fields': ('categories',)}),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Termin, TerminAdmin)
admin.site.register(RecurringTermin, RecurringTerminAdmin)

