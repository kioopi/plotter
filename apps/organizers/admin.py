from django.contrib import admin
from models import Organizer

class OrganizerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=('name','location')
    list_filter=('location',)
    search_fields=('name','description','url' )
    fieldsets=(
       (None, {'fields': ('name', 'slug', 'description', )}),
       ('Kontakt', {'fields': ('url', 'email', 'tel', 'location')}),
     #  ('Kontaktdaten', {'fields': ('url', 'email', 'phone', 'location')}),
     #  (None, {'fields': ('show_in_list',)}),
    )
admin.site.register(Organizer, OrganizerAdmin)

