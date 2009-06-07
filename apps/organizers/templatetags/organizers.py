from django import template

register = template.Library()

def as_link(org):
    return '<a href="%s">%s</a>' % ( org.get_absolute_url(), org.name )

def organizers_list(orgs):
    if not orgs: return ''
    linklist = [as_link(o) for o in orgs]
    if len(linklist) > 2:
       last = linklist.pop()
    else:
       last = None
    str =  ', '.join(linklist)
    if last: str += ' und ' + last
    return str
register.simple_tag(organizers_list)
