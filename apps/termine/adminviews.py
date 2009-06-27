#  Viewws tp extend the admin-interface.
#

from models import Termin, Category, RecurringTermin

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


from urllib import urlopen 

def rule_preview(request, id): 
    """Returns an HTML-Fragment with a list of the upcoming dated of the rule identified by id"""  
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/admin/')

    rt = get_object_or_404(RecurringTermin, pk = int(id))
    rule = rt.rrule
    html = '<ul><li>%s</li></ul>' % '</li><li>'.join([d.strftime('%A %d.%m.%Y') for d in rule])
    return HttpResponse(html)


def create_instances(request, id): 
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/admin/')

    rt = get_object_or_404(RecurringTermin, pk = int(id))
    rt.generate_dates() 



def get_osm_nodes(request, left, bottom, right, top): 
    xapi = 'http://xapi.openstreetmap.org/api/0.5'

    urltemplate = xapi + '/node[amenity=*][leisure=*][bbox=%s,%s,%s,%s]'     

    #urltemplate = 'http://xapi.openstreetmap.org/api/0.5/map?bbox=%s,%s,%s,%s' 

    url = urltemplate % (left,bottom,right,top)
   
    # FIXME needs a check if server's on and call successful
    # TODO cache results from osm to keep load off their servers
    xmldata = urlopen( url ).read() 
    print 
    print url
    
    return HttpResponse(xmldata, mimetype="application/xml") 
    
     
    
