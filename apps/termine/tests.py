"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Termin, RecurringTermin, WEEKLY, Category

from datetime import datetime, date, time, timedelta
import dateutil

class TerminTest(TestCase):
    def setUp(self): 
       self.t = Termin(startdate=date(2008, 6, 24), 
                   summary='This is just a Test'
                   ) 
       self.t.save() 


    def test_slug(self):
        """
        Tests that a slug gets defined automaticly 
        """
        self.failUnlessEqual(self.t.slug, 'this-is-just-a-test')
         
        # it should still be possible to change the slug manually 
        self.t.slug = 'testentry' 
        self.t.save() 
        self.failUnlessEqual(self.t.slug, 'testentry')
           
    def test_duration(self):
        self.failUnlessEqual(self.t.duration, 0)
        self.t.starttime = time(12, 0)  
        self.t.enddate =  datetime(2008, 6, 24, 13, 0)
        self.t.save() 
        self.failUnlessEqual(self.t.duration, timedelta(hours=1))

    def test_startdatetime(self):
        """ the startdatetime-property should combine startdate and starttime"""
        self.t.starttime = time(12, 0)  
        self.t.save() 
        self.failUnlessEqual(self.t.startdatetime, datetime(2008, 6, 24, 12, 0))

    def test_enddatetime(self): 
        self.failUnlessEqual(self.t.enddatetime, self.t.startdatetime)
        self.t.starttime = time(12, 0)  
        self.t.save() 
        self.failUnlessEqual(self.t.enddatetime, self.t.startdatetime)
        self.t.enddate =  datetime(2008, 6, 24, 13, 0)
        self.t.save() 
        self.failUnlessEqual(self.t.enddatetime, datetime(2008, 6, 24, 13, 0))
          
       
         
 
class RecurringTerminTest(TestCase):
     def setUp(self): 
        self.rc = RecurringTermin(name="Monday Meeting", rule_description="Every Monday", frequency=WEEKLY, first_date=date(2009,6,8) )
 
        self.rc.starttime = time(18,20)
        self.rc.summary = "Monday Monday"
        self.rc.save() 


     def test_rrule(self):
        """
        Tests that a slug gets defined automaticly 
        """
        rr = dateutil.rrule.rrule(WEEKLY, dtstart=date(2009,6,8) )
        for i in range(self.rc.rrule.count()): 
	    self.failUnlessEqual(
               self.rc.rrule[i],
               rr[i] ) 

     def test_instance_creation(self):  
        """Make an instance of a RecurringTermin"""
        day = date(2009,6,15) 
        t = self.rc.create_instance(day) 
	self.failUnlessEqual(t.summary, self.rc.summary) 
	self.failUnlessEqual(t.startdatetime, datetime(2009,6,15,18,20)) 

        # set the date to be 1h 10min long 
        self.rc.duration = 70   
        self.rc.save() 
        t = self.rc.create_instance(day) 
	self.failUnlessEqual(t.enddate, datetime(2009,6,15,19,30)) 

     def test_copy_m2m_fields(self):  
        """Test that categories in the recurringTermin are correctly copied over
           to the instatiated Termin"""
        cat1 = Category(name="Humpty") 
        cat1.save() 
        cat2 = Category(name="Dumpty") 
        cat2.save() 
       
        self.rc.categories.add(cat1)  
        self.rc.categories.add(cat2)  
        self.rc.save() 

        t = self.rc.create_instance(date(2009,6,15)) 
        cats = list(t.categories.all()) 
                  
        self.assert_(cat1 in cats) 
        self.assert_(cat2 in cats) 
  
       
 
 
         
        
    
            
 



__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

