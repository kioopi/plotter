
from south.db import db
from django.db import models
from locations.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('locations_city', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
            ('slug', models.SlugField(max_length=100)),
            ('lat', models.FloatField(null=True, blank=True)),
            ('long', models.FloatField(null=True, blank=True)),
            ('text', models.TextField(null=True, blank=True)),
        ))
        db.send_create_signal('locations', ['City'])
        
        # Adding model 'Location'
        db.create_table('locations_location', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
            ('slug', models.SlugField()),
            ('city', models.ForeignKey(orm.City)),
            ('adress', models.CharField("Adresse", max_length=250, blank=True)),
            ('zipcode', models.CharField("PLZ", max_length=20, blank=True)),
            ('lat', models.FloatField(null=True, blank=True)),
            ('long', models.FloatField(null=True, blank=True)),
            ('display_in_list', models.BooleanField("Anzeigen", default=True)),
            ('text', models.TextField(null=True, blank=True)),
        ))
        db.send_create_signal('locations', ['Location'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'City'
        db.delete_table('locations_city')
        
        # Deleting model 'Location'
        db.delete_table('locations_location')
        
    
    
    models = {
        'locations.city': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'lat': ('models.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'long': ('models.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'slug': ('models.SlugField', [], {'max_length': '100'}),
            'text': ('models.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'locations.location': {
            'adress': ('models.CharField', ['"Adresse"'], {'max_length': '250', 'blank': 'True'}),
            'city': ('models.ForeignKey', ["orm['locations.City']"], {}),
            'display_in_list': ('models.BooleanField', ['"Anzeigen"'], {'default': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'lat': ('models.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'long': ('models.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'slug': ('models.SlugField', [], {}),
            'text': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('models.CharField', ['"PLZ"'], {'max_length': '20', 'blank': 'True'})
        }
    }
    
    complete_apps = ['locations']
