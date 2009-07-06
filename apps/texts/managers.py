from django.db import models
from datetime import datetime

class OnlineManager(models.Manager):
    """Returns a queryset with publish-flagged texts with pubdate in the past"""
    def get_query_set(self):
      return super(OnlineManager,
                  self).get_query_set().filter(published=True).filter(pubdate__lte=datetime.now())
