from django.db import models
from locations.models import  Location
from django.template.defaultfilters import slugify
import datetime
from django.conf import settings

from locations.models import Location

class Organizer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField('Text', blank=True)
    url = models.URLField(blank=True, null=True) 

    email = models.EmailField(max_length=150, blank=True)
    tel = models.CharField(max_length=20, blank=True)

    location = models.ForeignKey(Location, blank=True, null=True)

    def upcoming_termine(self):
        return self.termin_set.filter(startdate__gte=datetime.date.today()).filter(publish=True)

    def __unicode__(self):
        return self.name

    # TODO: reverse-lookup this
    def get_absolute_url(self):
        return '/gruppen/%s/' % self.slug

    def save(self, force_insert=False, force_update=False):
        """Saves the City and takes care that there is a slug"""
        if not self.slug:
           self.slug = slugify(self.name)
        if self.url:
           # sanitize the url
           if not self.url.startswith('http') and not self.url.startswith('/'):
               from urlparse import urljoin
               self.url = urljoin('http', self.url)
        super(Organizer, self).save(force_insert, force_update)


    class Meta:
        ordering=['name']
        verbose_name="Gruppe"
        verbose_name_plural="Gruppen"

