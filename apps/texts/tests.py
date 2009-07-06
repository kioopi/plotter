"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase


class TextTest(TestCase): 
    def test_slug(self):
        """
        Tests that a slug gets defined automaticly 
        """
        self.t = Text(title="Ein langer Text", text="ist lang.") 
        self.t.save()
        self.failUnlessEqual(self.t.slug, 'ein-langer-text')

        # it should still be possible to change the slug manually 
        self.t.slug = 'testentry'
        self.t.save()
        self.failUnlessEqual(self.t.slug, 'testentry')



    def test_online_objects_manager(self): 
        self.fail()
