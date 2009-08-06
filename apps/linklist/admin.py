from django.contrib import admin
from models import Category, Link

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CatAdmin) 
admin.site.register(Link) 
