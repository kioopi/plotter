from django.conf.urls.defaults import *
from models import Termin, RecurringTermin
from datetime import date


# dict for single termin
termine_detail_dict = {
   'queryset': Termin.objects.select_related('location').all(),
   'slug_field': 'slug', 
   'date_field': 'startdate',
   'month_format' : '%m', 
   'allow_future' : True, 
}

# dict for month and day archives
termine_month_dict = {
   'queryset': Termin.objects.select_related('location').filter(publish=True),
   'date_field': 'startdate',
   'month_format' : '%m', 
   'allow_future' : True, 
   'allow_empty' : True, 
   'template_name': 'termine/termin_archive_month.html',
}

# dict for displaying this month
this_month_dict = termine_month_dict.copy() 
td = date.today() 
this_month_dict['year'] = td.year
this_month_dict['month'] = td.month


# ##########  patterns for display of  dates 
urlpatterns = patterns('',
  # einzerlner termin
  # wird durch datum und slug identifiziert
  # /termine/2009-07-22/terminslug/ 
  url(r'^(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', termine_detail_dict, name="termin_detail" ) ,
  #url(r'^(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 'apps.termine.views.detail', name="termin_detail" ) ,

  # --------------------------------------------------
  # termine eines monats 
  # /termine/2009-07-22/
   url(
     r'(?P<year>\d{4})-(?P<month>\d{1,2})/$',
     'django.views.generic.date_based.archive_month', 
     termine_month_dict,
   ),
   # termine eines monats, mit filterung nach category
   # /termine/2009-07-22/cat/catname/
   url(
     r'(?P<year>\d{4})-(?P<month>\d{1,2})/cat/(?P<cat>[-\w]+)/$',
     'apps.termine.views.month',
     termine_month_dict,
   ),

  # --------------------------------------------------
  # termine eines tages
  # es wird das gleiche template wie fuer das monatsarchiv verwendet 
  # /termine/2009-07-22/
  url(r'^(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', 'django.views.generic.date_based.archive_day', termine_month_dict ),

  # /termine/2009-07-22/cat/catname/ 
  url(r'^(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/cat/(?P<cat>[-\w]+)/$', 'apps.termine.views.day', termine_month_dict ),


  # die naechsten n termine 

  # umleitung von /termin
  
  url(r'^$',   
    'django.views.generic.date_based.archive_month', 
     this_month_dict,
  ) 
) 

# ###################### patterns for recurring dates 
urlpatterns += patterns('',
  url('^regulars/$', 'termine.views.recurring_dates_list'), 
  url('^regulars/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail',{ 
      'queryset': RecurringTermin.objects.all(), 
  }), 
  


)

# ################# patterns for extending the admin interface 
urlpatterns += patterns('',
   # /termine/rules/12/preview/ 
   # preview on the future dates of a rule
   url(r'^rules/(?P<id>\d+)/preview/$',   
    'apps.termine.adminviews.rule_preview', 
  ),

   # /termine/rules/12/preview/ 
   # preview on the future dates of a rule
   url(r'^rules/(?P<id>\d+)/createdates/$',   
    'apps.termine.adminviews.create_instances', 
  ),


  # /termine/getosmnodes/50.343,6.123213,50.231,6.232/
  # return osm-xml containing nodes for the bbox
   url(r'getosmnodes/([\d\.]+),([\d\.]+)-([\d\.]+),([\d\.]+)/',
      'apps.termine.adminviews.get_osm_nodes', 
   )




)
