from django import template
from locations.models import Location

register = template.Library() 

@register.inclusion_tag('admin/locations/inclusion_map.html')
def display_map(location_id): 
    object = Location.objects.get(id__exact=location_id)
    return {'object': object} 

