from django.db import models
from datetime import datetime

from managers import OnlineManager

class Text(models.Model):
    """Post model."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)  
    
    tease = models.TextField(blank=True) 
    text = models.TextField() 

    author_name = models.CharField(max_length=200, blank=True, default="Anonymous")

    pubdate = models.DateTimeField()
    published = models.BooleanField(default=True) 

    online_objects = OnlineManager() 
    objects = models.Manager()  # is this really necc


    class Meta:
        verbose_name_plural = 'Texte'
        ordering            = ('-pubdate',)
        get_latest_by       = 'pubdate'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self): 
        return '/texte/%s/' % self.slug 

