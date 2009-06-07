from django.contrib import admin
from models import Category, Termin

class TerminAdmin(admin.ModelAdmin):
    list_display = ('summary','startdate', 'publish')
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Termin, TerminAdmin)

