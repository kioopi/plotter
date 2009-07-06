from django.conf.urls.defaults import *
from models import Text


info = {
    'queryset': Text.online_objects.all(),
}


urlpatterns = patterns('django.views.generic.list_detail',
   url(
       r'^$',
       'object_list',
       info ,
       name='text_list'
   ),
   url(
       r'^(?P<slug>[-\w]+)/$',
       'object_detail',
       info,
       name='text_detail'
   ),

)
