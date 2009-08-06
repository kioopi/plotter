from django.conf.urls.defaults import *
from linklist.models import Category

info = {
    'queryset': Category.objects.all(),
}

urlpatterns = patterns('', 
   url(r'^$', 
       'django.views.generic.list_detail.object_list',  
       info, 
       name='link_list'
   ) 
) 
