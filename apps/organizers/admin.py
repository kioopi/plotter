from django.contrib import admin
from models import Organizer

class OrganizerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=('name',)
    search_fields=('name','description','url' )
    fieldsets=(
       (None, {'fields': ('name', 'slug', 'description', 'url')}),
     #  ('Kontaktdaten', {'fields': ('url', 'email', 'phone', 'location')}),
     #  (None, {'fields': ('show_in_list',)}),
    )
admin.site.register(Organizer, OrganizerAdmin)

