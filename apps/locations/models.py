from django.db import models

from django.template.defaultfilters import slugify
from django.db.models import permalink

from django.conf import settings
import datetime


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    text = models.TextField(blank=True, null=True)

    class Meta:
       verbose_name="Stadt"
       verbose_name_plural="Staedte"

    def __unicode__(self):
       return self.name

    def save(self, force_insert=False, force_update=False):
        """Saves the City and takes care that there is a slug"""
        if not self.slug:
           self.slug = slugify(self.name)
        if not self.lat:
           self.geocode();
        super(City, self).save(force_insert, force_update)

    def geocode(self):
        from geopy import geocoders
        g = geocoders.Google(settings.GOOGLE_API_KEY)
        adress = u'%s, germany' % (self.name)
        try:
            place, (lat, lng) = g.geocode(adress.encode("latin-1"), exactly_one=True)
        except:
            return False
        if lat and lng:
            self.lat = lat
            self.long = lng
            return True
        return False


STATIC_MAPS_SIZE = '150x150' #FIXME: settings go in settings.py



class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    city = models.ForeignKey('City', verbose_name="Stadt")

    adress = models.CharField("Adresse", max_length=250, blank=True)
    zipcode = models.CharField("PLZ",max_length=20, blank=True)
    lat     = models.FloatField(blank=True, null=True)
    long    = models.FloatField(blank=True, null=True)

    display_in_list = models.BooleanField("Anzeigen",default=True)

    text = models.TextField(blank=True, null=True)

    def upcoming_termine(self):
        return self.termin_set.filter(startdate__gte=datetime.date.today()).filter(publish=True)


    # TODO locally safe the map-pictures?
    def static_map_url(self):
        if self.lat and self.long:
            url = 'http://maps.google.com/staticmap?markers=%f,%f&size=%s&zoom=14&key=%s' % (self.lat, self.long, STATIC_MAPS_SIZE, settings.GOOGLE_API_KEY)
        else:
            url = False
        return url
        

    class Meta:
       verbose_name="Ort"
       verbose_name_plural="Orte"

    def save(self):
        """Saves the Location and takes care that there is a slug"""
        if not self.slug:
           self.slug = slugify(self.name)
        if not self.lat:
           self.geocode()
        super(Location, self).save()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ('location_detail',(), {'slug': self.slug})
    get_absolute_url = permalink(get_absolute_url)

    def geocode(self):
        from geopy import geocoders
        g = geocoders.Google(settings.GOOGLE_API_KEY)
        adress = u'%s, %s %s, germany' % (self.adress, self.zipcode, self.city)
        try:
            place, (lat, lng) = g.geocode(adress.encode("latin-1"), exactly_one=True)
        except:
            return False
        if lat and lng:
            self.lat = lat
            self.long = lng
            return True
        return False




