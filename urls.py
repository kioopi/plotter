from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
   # (r'^plotter2010/', include('plotter2010.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^admin/(.*)', admin.site.root),

    (r'^termine/', include('plotter2010.apps.termine.urls')),
    (r'^gruppen/', include('plotter2010.apps.organizers.urls')),
    (r'^orte/', include('plotter2010.apps.locations.urls')),
    (r'^texte/', include('plotter2010.apps.texts.urls')),
    (r'^links/', include('plotter2010.apps.linklist.urls')),
)

from django.conf import settings
# this is for testing with the development server only 
# serving media via the django-testserver 
if settings.DEVELOPMENT:
    urlpatterns += patterns('',
        (r'^sitemedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.LOCAL_MEDIA}),
    )

