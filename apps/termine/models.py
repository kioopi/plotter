from django.db import models

from django.db.models import permalink

from django.template.defaultfilters import slugify
from datetime import datetime, timedelta, time, date

from django.conf import settings


from django.contrib.auth.models import User

from organizers.models import Organizer
from locations.models import  Location

from dateutil import rrule 
 

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
    """BaseTermin is an abstract model to DRY the date-payload in an actual
       Termin and the rule for recurring dates (RecurringTermin)"""

    starttime    = models.TimeField("Uhrzeit", blank=True, null=True)
    summary      = models.CharField("Titel", unique_for_date='startdate', max_length=250)
    description  = models.TextField("Text",blank=True)
    location     = models.ForeignKey(Location, verbose_name="Ort", blank=True, null=True)

    organizers = models.ManyToManyField('organizers.Organizer', blank=True, verbose_name="Gruppe")

    categories = models.ManyToManyField('Category', blank=True, verbose_name="Kategorien")

    # technical fields
    owner = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract=True

class Termin(BaseTermin):
    """Represents one Date in the Calendar. Is derived from BaseTermin to ensure consistancy with RecurringTermin"""

    startdate    = models.DateField("Datum")
    enddate      = models.DateTimeField("Enddatum und Uhrzeit", blank=True, null=True)
    slug = models.SlugField(unique_for_date='startdate')

    rule = models.ForeignKey("RecurringTermin", blank=True, null=True, related_name="instances")

    publish = models.BooleanField("Veroeffentlichen",default=True)

    # should there be special fields for musical events like 'performer'?
    # sould there be a field for a entry-fee?
    class Meta:
        get_latest_by = 'startdate'
        ordering = ['startdate', 'starttime', 'location', 'slug']
        verbose_name="Termin"
        verbose_name_plural="Termine"


    def _get_duration(self):
        if not self.enddate:
            return 0
        else:
            return self.enddate-self.startdatetime
    duration = property(_get_duration) 

    def _get_enddatetime(self):  
        if self.enddate: 
            return self.enddate 
        return self.startdatetime 
    enddatetime = property(_get_enddatetime) 
     

    def _get_startdatetime(self):
        "Returns a datetime object for the start-date and time of the date"
        if self.starttime:
            return datetime.combine(self.startdate, self.starttime)
        else:
            return datetime.combine(self.startdate, time(0,0))
    startdatetime = property(_get_startdatetime) 

    def save(self):
        """Saves the Date and takes care that there is a slug"""
        if not self.slug:
           self.slug = slugify(self.summary)
        super(Termin, self).save()

    def __unicode__(self):
        return '%s - %s' % (self.startdate.strftime('%d.%m.%Y'), self.summary)

    def get_absolute_url(self):
        return ('termin_detail', (), {
            'year': self.startdate.year,
            'month': self.startdate.month,
            'day': self.startdate.day,
            'slug': self.slug})
    get_absolute_url = permalink(get_absolute_url)

# dateutil.rrule works internally with integers for rule frequencies.
(YEARLY,
 MONTHLY,
 WEEKLY,
 DAILY,
 HOURLY,
 MINUTELY,
 SECONDLY) = range(7)

# a mapping to german text.
FREQ_CHOICES = (
  ( YEARLY, 'Jaehrlich'),
  ( MONTHLY, 'Monatlich'),
  ( WEEKLY, 'Woechentlich'),
  ( DAILY, 'Taeglich'),
)

class RecurringTermin(BaseTermin): 
    """A rule for reccuring dates. from this model actual dates (Termin) can be instatiated.
    
       Uses dateutils rrule
    """
    name = models.CharField(max_length=100)

    # a plain text description of the rule 
    # "Jeden Sonntag um 11.00 Uhr"  
    rule_description = models.CharField(max_length=200)

    # repetition frequency of the recurring date 
    frequency = models.IntegerField(choices=FREQ_CHOICES, max_length=10)
    # first date of the series
    first_date   = models.DateField()
    # date takes place every 'interval'th repetition 
    interval = models.IntegerField(default=1)

    # repetition must coincide with given weekdays. 
    byweekday = models.CharField(max_length=20, blank=True)

    # duration of an instance in minutes
    duration = models.IntegerField('Dauer', blank=True, null=True) 
    
    # new dates should be instatiated `createdelta` days before  
    # their occurance  
    createdelta  = models.IntegerField(default=14)

    # remember the latest instance created from this rule, so 
    # only dates further in the future are created afterwards 
    last_created = models.ForeignKey(Termin, related_name="latest_instance",
                     blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
  
    def get_absolute_url(self):  
        return '/termine/regulars/%d/' % self.id 

    def create_instance(self, day):    
        """Takes a date-object and creates a instance (Termin) of this rule on this day""" 
          
        #FIXME maybe BaseTermin should be introspected here to DRY this out a little. 
	enddate=datetime.combine(day, self.starttime)
        if self.duration: 
            enddate += timedelta(minutes=self.duration) 

        t = Termin( 
           summary = self.summary, 
           startdate=day,
           starttime=self.starttime,
           enddate=enddate,
           description=self.description,
           location=self.location,
           rule=self
        )
        t.save()

        # copy organizers to instance
        for o in self.organizers.all():  
           t.organizers.add(o) 

        # copy cats to instance
        for c in self.categories.all():  
            t.categories.add(c) 
        
        # set the last_created field to the new generated date
        if not self.last_created or self.last_created.startdate < t.startdate:
            self.last_created = t
            self.save() 

        t.save()
        return t


    def string_to_weekday_obj(self, wstr):  
        """""" 
        WD_CONSTANTS = (MO, TU, WE, TH, FR, SA, SO )
       
        # if weekday was passed in as a two-char-abbr
        if wstr.upper() in WD_CONSTANTS: 
            return getattr(dateutil.rrule, wstr.upper()) 

        try: 
           # if weekday was a number 0=monday 
           return getattr(dateutil.rrule, WD_CONSTANTS(int(wstr))) 
        except ValueError: 
           # if weekday came as constant with parameter MO(2) 
           wd, num = wstr.split('(') 
           num = int(num[:-1]) # cut off the last char  )  and convert to int
           return getattr(datetutil.rrule, wd.upper())(num)
           
   

    def get_rrule(self, end=False): 
        """Returns an rrule object for this rule. """ 

        # FIXME build a cacheing for the rrule 

        # kw-arguments for the object's constructor are collected in a dictionary
        kwargs = {}  
        
        # rrule starting at either the first day of this ReccuringTermin or 
        # at the date of the last created instance 
        if self.last_created:
            kwargs['dtstart'] = self.last_created.startdate
        else:
            kwargs['dtstart'] = self.first_date
 
        # the last date to be generated by the rrule should be createdelta 
        # days after the first day (unless overwritten by the argument end)   
        if end:
            kwargs['until'] = end
        else:
            kwargs['until'] = kwargs['dtstart']+timedelta(days=self.createdelta)
        
        # interval
        kwargs['interval'] = int(self.interval)

        # byweekday field is a little weird
        # different kinds of input are accepted
        # numbers:   0, 3, 4
        # constants  MO, TH, FR
        # constats with params:  MO(1), TH(10), FR(-1) 
        if self.byweekday: 
            by_wd = [] 
            for wd in self.byweekday.split(','):  
               by_wd.append(self.string_to_weekday_obj(wd)) 
            kwargs['byweekday'] = by_wd   
                
        return rrule.rrule(int(self.frequency), **kwargs)
    rrule = property(get_rrule) 


    def generate_dates(self):
        """Creates upcoming instances for this rule.""" 
        for d in self.rrule():
            d = datetime.date(d)
            self.create_instance(d)



