from django.conf.urls.defaults import *
from models import Text


info = {
    'queryset': Text.online_objects.all(),
}


urlpatterns = patterns('django.views.generic.list_detail',
  url(
       r'^(?P<slug>[-\w]+)/$',
       'object_detail',
       info,
       name='text_detail'
   ),

)

dinfo = {
    'queryset': Text.online_objects.all(),
    'date_field': 'pubdate', 
    'num_latest': 20, 
}

urlpatterns += patterns('django.views.generic.date_based',
   url(
       r'^$',
       'archive_index',
       dinfo ,
       name='text_list'
   ),
) 
