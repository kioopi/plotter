#  Viewws tp extend the admin-interface.
#

from models import Termin, Category, RecurringTermin

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


def rule_preview(request, id): 
    """Returns an HTML-Fragment with a list of the upcoming dated of the rule identified by id"""  
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/admin/')

    rt = get_object_or_404(RecurringTermin, pk = int(id))
    rule = rt.rrule() 
    html = '<ul><li>%s</li></ul>' % '</li><li>'.join([d.strftime('%A %d.%m.%Y') for d in rule])
    return HttpResponse(html)

