
from south.db import db
from django.db import models
from texts.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Text'
        db.create_table('texts_text', (
            ('id', orm['texts.Text:id']),
            ('title', orm['texts.Text:title']),
            ('slug', orm['texts.Text:slug']),
            ('tease', orm['texts.Text:tease']),
            ('text', orm['texts.Text:text']),
            ('author_name', orm['texts.Text:author_name']),
            ('pubdate', orm['texts.Text:pubdate']),
            ('published', orm['texts.Text:published']),
        ))
        db.send_create_signal('texts', ['Text'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Text'
        db.delete_table('texts_text')
        
    
    
    models = {
        'texts.text': {
            'author_name': ('django.db.models.fields.CharField', [], {'default': "'Anonymous'", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'tease': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['texts']
