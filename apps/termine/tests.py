"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Termin 

from datetime import datetime, date, time, timedelta

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
          
       
         
 
 



__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

