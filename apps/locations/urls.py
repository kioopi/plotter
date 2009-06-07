from django.conf.urls.defaults import *
from locations.models import Location

location_info = {
    'queryset': Location.objects.filter(display_in_list=True),
}


urlpatterns = patterns('', 
   url(r'^findgeo/', 'locations.views.geocode'),  
) 

urlpatterns += patterns('django.views.generic.list_detail',
   url(
       r'^$',
       'object_list',
       location_info ,
       name='location_list'
   ),
   url(
       r'^(?P<slug>[-\w]+)/$',
       'object_detail',
       location_info,
       name='location_detail'
   ),

 
) 
