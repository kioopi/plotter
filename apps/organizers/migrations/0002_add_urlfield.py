
from south.db import db
from django.db import models
from organizers.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Organizer.url'
        db.add_column('organizers_organizer', 'url', models.URLField(blank=True, null=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Organizer.url'
        db.delete_column('organizers_organizer', 'url')
        
    
    
    models = {
        'organizers.organizer': {
            'Meta': {'ordering': "['name']"},
            'description': ('models.TextField', ["'Text'"], {'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'slug': ('models.SlugField', [], {}),
            'url': ('models.URLField', [], {'blank': 'True'})
        }
    }
    
    complete_apps = ['organizers']
