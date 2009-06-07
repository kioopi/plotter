
from south.db import db
from django.db import models
from locations.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('locations_city', (
            ('name', models.CharField(max_length=100)),
            ('text', models.TextField(null=True, blank=True)),
            ('long', models.FloatField(null=True, blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('lat', models.FloatField(null=True, blank=True)),
            ('slug', models.SlugField(max_length=100)),
        ))
        db.send_create_signal('locations', ['City'])
        
        # Adding model 'Location'
        db.create_table('locations_location', (
            ('city', models.ForeignKey(orm.City, verbose_name="Stadt")),
            ('name', models.CharField(max_length=100)),
            ('text', models.TextField(null=True, blank=True)),
            ('display_in_list', models.BooleanField("Anzeigen", default=True)),
            ('zipcode', models.CharField("PLZ", max_length=20, blank=True)),
            ('long', models.FloatField(null=True, blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('lat', models.FloatField(null=True, blank=True)),
            ('adress', models.CharField("Adresse", max_length=250, blank=True)),
            ('slug', models.SlugField()),
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
            'city': ('models.ForeignKey', ["'City'"], {'verbose_name': '"Stadt"'}),
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
