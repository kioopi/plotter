from django.db import models
#from django.conf import settings
import termine 
from django.template.defaultfilters import slugify


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


class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField() 
    categories = models.ManyToManyField('Category', verbose_name="Kategorien")

    class Meta:
        ordering = ['name']
