from models import Termin, Category

from django.views.generic.date_based import object_detail, archive_month, archive_day  

from django.views.generic.date_based import archive_month
def month(request, **kwargs): 
    """ uses the date-based generic view archive_month, but filters the queryset 
        by category

        uses all the same parameters as archive_month from the url-conf  
    """
    year = kwargs.pop('year') 
    month = kwargs.pop('month') 
    date_field = kwargs.pop('date_field') 
    queryset = kwargs.pop('queryset') 
 
    if not kwargs.get("extra_context", False): 
        kwargs["extra_context"] = {}
 
    if kwargs.get('cat', False):
        cat = kwargs.pop('cat') 
        queryset = queryset.filter(categories__slug=cat)
	kwargs["extra_context"]["cat"] = Category.objects.get(slug=cat) 
    return archive_month(request, year, month, queryset, date_field, **kwargs)  



def day(request, **kwargs): 
    """ uses the date-based generic view archive_day, but filters the queryset 
        by category

        uses all the same parameters as archive day from the url-conf  
    """
    year = kwargs.pop('year') 
    month = kwargs.pop('month') 
    day = kwargs.pop('day') 
    date_field = kwargs.pop('date_field') 
    queryset = kwargs.pop('queryset') 
 
    if not kwargs.get("extra_context", False): 
        kwargs["extra_context"] = {}
 
    if kwargs.get('cat', False):
        cat = kwargs.pop('cat') 
        queryset = queryset.filter(categories__slug=cat)
	kwargs["extra_context"]["cat"] = Category.objects.get(slug=cat) 
    return archive_day(request, year, month, day, queryset, date_field, **kwargs)  


