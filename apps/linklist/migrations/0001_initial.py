
from south.db import db
from django.db import models
from linklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('linklist_link', (
            ('id', orm['linklist.Link:id']),
            ('link', orm['linklist.Link:link']),
            ('name', orm['linklist.Link:name']),
            ('description', orm['linklist.Link:description']),
        ))
        db.send_create_signal('linklist', ['Link'])
        
        # Adding model 'Category'
        db.create_table('linklist_category', (
            ('id', orm['linklist.Category:id']),
            ('name', orm['linklist.Category:name']),
            ('slug', orm['linklist.Category:slug']),
        ))
        db.send_create_signal('linklist', ['Category'])
        
        # Adding ManyToManyField 'Link.categories'
        db.create_table('linklist_link_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('link', models.ForeignKey(orm.Link, null=False)),
            ('category', models.ForeignKey(orm.Category, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('linklist_link')
        
        # Deleting model 'Category'
        db.delete_table('linklist_category')
        
        # Dropping ManyToManyField 'Link.categories'
        db.delete_table('linklist_link_categories')
        
    
    
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
