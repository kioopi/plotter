
from south.db import db
from django.db import models
from termine.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Termin'
        db.create_table('termine_termin', (
            ('startdate', models.DateField("Datum")),
            ('enddate', models.DateTimeField("Enddatum und Uhrzeit", null=True, blank=True)),
            ('description', models.TextField("Text", blank=True)),
            ('created', models.DateTimeField(auto_now_add=True)),
            ('modified', models.DateTimeField(auto_now=True)),
            ('publish', models.BooleanField("Veroeffentlichen", default=True)),
            ('id', models.AutoField(primary_key=True)),
            ('location', models.ForeignKey(orm['locations.Location'], null=True, verbose_name="Ort", blank=True)),
            ('starttime', models.TimeField("Uhrzeit", null=True, blank=True)),
            ('owner', models.ForeignKey(orm['auth.User'], null=True, blank=True)),
            ('summary', models.CharField("Titel", max_length=250, unique_for_date='startdate')),
            ('slug', models.SlugField(unique_for_date='startdate')),
        ))
        db.send_create_signal('termine', ['Termin'])
        
        # Adding model 'Category'
        db.create_table('termine_category', (
            ('slug', models.SlugField()),
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
        ))
        db.send_create_signal('termine', ['Category'])
        
        # Adding ManyToManyField 'Termin.organizers'
        db.create_table('termine_termin_organizers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('termin', models.ForeignKey(Termin, null=False)),
            ('organizer', models.ForeignKey(Organizer, null=False))
        ))
        
        # Adding ManyToManyField 'Termin.categories'
        db.create_table('termine_termin_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('termin', models.ForeignKey(Termin, null=False)),
            ('category', models.ForeignKey(Category, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Termin'
        db.delete_table('termine_termin')
        
        # Deleting model 'Category'
        db.delete_table('termine_category')
        
        # Dropping ManyToManyField 'Termin.organizers'
        db.delete_table('termine_termin_organizers')
        
        # Dropping ManyToManyField 'Termin.categories'
        db.delete_table('termine_termin_categories')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'termine.termin': {
            'Meta': {'ordering': "['startdate','starttime','location','slug']", 'get_latest_by': "'startdate'"},
            'categories': ('models.ManyToManyField', ["'Category'"], {'verbose_name': '"Kategorien"', 'blank': 'True'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', ['"Text"'], {'blank': 'True'}),
            'enddate': ('models.DateTimeField', ['"Enddatum und Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'location': ('models.ForeignKey', ['Location'], {'null': 'True', 'verbose_name': '"Ort"', 'blank': 'True'}),
            'modified': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'organizers': ('models.ManyToManyField', ["'organizers.Organizer'"], {'verbose_name': '"Gruppe"', 'blank': 'True'}),
            'owner': ('models.ForeignKey', ['User'], {'null': 'True', 'blank': 'True'}),
            'publish': ('models.BooleanField', ['"Veroeffentlichen"'], {'default': 'True'}),
            'slug': ('models.SlugField', [], {'unique_for_date': "'startdate'"}),
            'startdate': ('models.DateField', ['"Datum"'], {}),
            'starttime': ('models.TimeField', ['"Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'summary': ('models.CharField', ['"Titel"'], {'max_length': '250', 'unique_for_date': "'startdate'"})
        },
        'locations.location': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'termine.category': {
            'Meta': {'ordering': "['name']"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'slug': ('models.SlugField', [], {})
        },
        'organizers.organizer': {
            'Meta': {'ordering': "['name']"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['termine']
