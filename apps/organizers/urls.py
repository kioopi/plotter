from django.conf.urls.defaults import *
from organizers.models import Organizer

organizer_info = {
    'queryset': Organizer.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
   url(
       r'^$',
       'object_list',
       organizer_info,
       name='organizers_index'
   ),
   url(
       r'^(?P<slug>[-\w]+)/$',
       'object_detail',
       organizer_info,
       name='organizers_detail'
   ),

)

