from django.db import models

from django.db.models import permalink

from django.template.defaultfilters import slugify
from datetime import datetime, timedelta, time, date

from django.conf import settings


from django.contrib.auth.models import User

from organizers.models import Organizer
from locations.models import  Location
 

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ['name'] 
        verbose_name="Kategorie"
        verbose_name_plural="Kategorien"

    def __unicode__(self):
        return self.name

    def save(self):
        """Saves the Category and takes care that there is a slug"""
        if not self.slug:
           self.slug = slugify(self.name)
        super(Category, self).save()


class BaseTermin(models.Model):
    # ical-related fields
    starttime    = models.TimeField("Uhrzeit", blank=True, null=True)
    summary      = models.CharField("Titel", unique_for_date='startdate', max_length=250)
    description  = models.TextField("Text",blank=True)
    location     = models.ForeignKey(Location, verbose_name="Ort", blank=True, null=True)

    organizers = models.ManyToManyField('Organizer', blank=True, verbose_name="Gruppe")
    categories = models.ManyToManyField('Category', blank=True, verbose_name="Kategorien")


    class Meta:
        abstract=True


class Termin(BaseTermin):
    """Represents one Date in the Calendar"""
    slug = models.SlugField(unique_for_date='startdate')

    startdate    = models.DateField("Datum")
    enddate      = models.DateTimeField("Enddatum und Uhrzeit", blank=True, null=True)
#    regular = models.ForeignKey("Regular", blank=True, null=True, related_name="belongs_to")


    # technical fields
    owner = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    publish = models.BooleanField("Veroeffentlichen",default=True)

    # should there be special fields for musical events like 'performer'?
    # sould there be a field for a entry-fee?
    class Meta:
        get_latest_by = 'startdate'
        ordering = ['startdate', 'starttime', 'location', 'slug']
        verbose_name="Termin"
        verbose_name_plural="Termine"


    def duration(self):
        if not self.enddate:
            return 0
        else:
            return self.enddate-self.startdatetime()

    def short_summary(self):
        if len(self.summary) >= 10:
            return self.summary[:7] + "..."
        else:
            return self.summary

    def startdatetime(self):
        "Returns a datetime object for the start-date and time of the date"
        if self.starttime:
            return datetime.combine(self.startdate, self.starttime)
        else:
            return datetime.combine(self.startdate, time(0,0))

    def save(self):
        """Saves the Date and takes care that there is a slug"""
        if not self.slug:
           self.slug = slugify(self.summary)
        super(Termin, self).save()
    def __unicode__(self):
        return '%s - %s' % (self.startdate.strftime('%d.%m.%Y'), self.summary)

    def get_absolute_url(self):
        return ('single_termin', (), {
            'year': self.startdate.year,
            'month': self.startdate.month,
            'day': self.startdate.day,
            'slug': self.slug})
    get_absolute_url = permalink(get_absolute_url)


