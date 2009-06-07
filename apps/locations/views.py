# Crea te your views here.


def geocode(request): 
    """ To be requested via xhr. 
        takes an adress an tries to geocode it returning the lat/lon pair.
    """ 
    from geopy import geocoders
    g = geocoders.Google(settings.GOOGLE_API_KEY)
    adress = u'%s, %s %s, germany' % (request.REQUEST['adress'],
                                      request.REQUEST['zipcode'],
                                      request.REQUEST['city'])
    try:
        place, (lat, lon) = g.geocode(adress.encode("latin-1"), exactly_one=True)
    except:
        return HttpResponse('{ok: false}', mimetype='application/json')

    if lat and lon: 
        json = "{ ok: true, place: '%s', lat: %f, long: %d }" % ( place, lat, lon )  
        return HttpResponse(json, mimetype='application/json')
    return HttpResponse('{ok: false}', mimetype='application/json')
