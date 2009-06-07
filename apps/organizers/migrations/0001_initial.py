
from south.db import db
from django.db import models
from organizers.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Organizer'
        db.create_table('organizers_organizer', (
            ('slug', models.SlugField()),
            ('description', models.TextField('Text', blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
        ))
        db.send_create_signal('organizers', ['Organizer'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Organizer'
        db.delete_table('organizers_organizer')
        
    
    
    models = {
        'organizers.organizer': {
            'Meta': {'ordering': "['name']"},
            'description': ('models.TextField', ["'Text'"], {'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'slug': ('models.SlugField', [], {})
        }
    }
    
    complete_apps = ['organizers']
