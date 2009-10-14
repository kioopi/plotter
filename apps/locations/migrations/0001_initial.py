
from south.db import db
from django.db import models
from locations.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('locations_city', (
            ('id', orm['locations.City:id']),
            ('name', orm['locations.City:name']),
            ('slug', orm['locations.City:slug']),
            ('lat', orm['locations.City:lat']),
            ('long', orm['locations.City:long']),
            ('text', orm['locations.City:text']),
        ))
        db.send_create_signal('locations', ['City'])
        
        # Adding model 'Location'
        db.create_table('locations_location', (
            ('id', orm['locations.Location:id']),
            ('name', orm['locations.Location:name']),
            ('slug', orm['locations.Location:slug']),
            ('city', orm['locations.Location:city']),
            ('adress', orm['locations.Location:adress']),
            ('zipcode', orm['locations.Location:zipcode']),
            ('lat', orm['locations.Location:lat']),
            ('long', orm['locations.Location:long']),
            ('display_in_list', orm['locations.Location:display_in_list']),
            ('text', orm['locations.Location:text']),
        ))
        db.send_create_signal('locations', ['Location'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'City'
        db.delete_table('locations_city')
        
        # Deleting model 'Location'
        db.delete_table('locations_location')
        
    
    
    models = {
        'locations.city': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'locations.location': {
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.City']"}),
            'display_in_list': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }
    
    complete_apps = ['locations']
