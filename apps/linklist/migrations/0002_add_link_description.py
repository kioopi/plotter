
from south.db import db
from django.db import models
from linklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Link.description'
        db.add_column('linklist_link', 'description', orm['linklist.link:description'])
        
        # Changing field 'Link.name'
        # (to signature: django.db.models.fields.CharField(max_length=100, blank=True))
        db.alter_column('linklist_link', 'name', orm['linklist.link:name'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Link.description'
        db.delete_column('linklist_link', 'description')
        
        # Changing field 'Link.name'
        # (to signature: django.db.models.fields.CharField(max_length=100))
        db.alter_column('linklist_link', 'name', orm['linklist.link:name'])
        
    
    
    models = {
        'linklist.category': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'linklist.link': {
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['linklist.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }
    
    complete_apps = ['linklist']
