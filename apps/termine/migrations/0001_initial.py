
from south.db import db
from django.db import models
from termine.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'RecurringTermin'
        db.create_table('termine_recurringtermin', (
            ('rule_description', models.CharField(max_length=200)),
            ('interval', models.IntegerField(default=1)),
            ('last_created', models.ForeignKey(orm.Termin, related_name="latest_instance", null=True, blank=True)),
            ('description', models.TextField("Text", blank=True)),
            ('created', models.DateTimeField(auto_now_add=True)),
            ('first_date', models.DateField()),
            ('modified', models.DateTimeField(auto_now=True)),
            ('summary', models.CharField("Titel", max_length=250, unique_for_date='startdate')),
            ('duration', models.IntegerField('Dauer', null=True, blank=True)),
            ('byweekday', models.CharField(max_length=20, blank=True)),
            ('frequency', models.IntegerField(max_length=10)),
            ('location', models.ForeignKey(orm['locations.Location'], null=True, verbose_name="Ort", blank=True)),
            ('starttime', models.TimeField("Uhrzeit", null=True, blank=True)),
            ('owner', models.ForeignKey(orm['auth.User'], null=True, blank=True)),
            ('createdelta', models.IntegerField(default=14)),
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
        ))
        db.send_create_signal('termine', ['RecurringTermin'])
        
        # Adding model 'Termin'
        db.create_table('termine_termin', (
            ('startdate', models.DateField("Datum")),
            ('slug', models.SlugField(unique_for_date='startdate')),
            ('enddate', models.DateTimeField("Enddatum und Uhrzeit", null=True, blank=True)),
            ('description', models.TextField("Text", blank=True)),
            ('created', models.DateTimeField(auto_now_add=True)),
            ('modified', models.DateTimeField(auto_now=True)),
            ('rule', models.ForeignKey(orm.RecurringTermin, related_name="instances", null=True, blank=True)),
            ('summary', models.CharField("Titel", max_length=250, unique_for_date='startdate')),
            ('location', models.ForeignKey(orm['locations.Location'], null=True, verbose_name="Ort", blank=True)),
            ('starttime', models.TimeField("Uhrzeit", null=True, blank=True)),
            ('owner', models.ForeignKey(orm['auth.User'], null=True, blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('publish', models.BooleanField("Veroeffentlichen", default=True)),
        ))
        db.send_create_signal('termine', ['Termin'])
        
        # Adding model 'Category'
        db.create_table('termine_category', (
            ('slug', models.SlugField()),
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
        ))
        db.send_create_signal('termine', ['Category'])
        
        # Adding ManyToManyField 'RecurringTermin.organizers'
        db.create_table('termine_recurringtermin_organizers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recurringtermin', models.ForeignKey(RecurringTermin, null=False)),
            ('organizer', models.ForeignKey(Organizer, null=False))
        ))
        
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
        
        # Adding ManyToManyField 'RecurringTermin.categories'
        db.create_table('termine_recurringtermin_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recurringtermin', models.ForeignKey(RecurringTermin, null=False)),
            ('category', models.ForeignKey(Category, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'RecurringTermin'
        db.delete_table('termine_recurringtermin')
        
        # Deleting model 'Termin'
        db.delete_table('termine_termin')
        
        # Deleting model 'Category'
        db.delete_table('termine_category')
        
        # Dropping ManyToManyField 'RecurringTermin.organizers'
        db.delete_table('termine_recurringtermin_organizers')
        
        # Dropping ManyToManyField 'Termin.organizers'
        db.delete_table('termine_termin_organizers')
        
        # Dropping ManyToManyField 'Termin.categories'
        db.delete_table('termine_termin_categories')
        
        # Dropping ManyToManyField 'RecurringTermin.categories'
        db.delete_table('termine_recurringtermin_categories')
        
    
    
    models = {
        'termine.termin': {
            'Meta': {'ordering': "['startdate','starttime','location','slug']", 'get_latest_by': "'startdate'"},
            'categories': '<< PUT FIELD DEFINITION HERE >>',
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', ['"Text"'], {'blank': 'True'}),
            'enddate': ('models.DateTimeField', ['"Enddatum und Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'location': ('models.ForeignKey', ['Location'], {'null': 'True', 'verbose_name': '"Ort"', 'blank': 'True'}),
            'modified': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'organizers': '<< PUT FIELD DEFINITION HERE >>',
            'owner': ('models.ForeignKey', ['User'], {'null': 'True', 'blank': 'True'}),
            'publish': ('models.BooleanField', ['"Veroeffentlichen"'], {'default': 'True'}),
            'rule': ('models.ForeignKey', ['"RecurringTermin"'], {'related_name': '"instances"', 'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'unique_for_date': "'startdate'"}),
            'startdate': ('models.DateField', ['"Datum"'], {}),
            'starttime': ('models.TimeField', ['"Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'summary': ('models.CharField', ['"Titel"'], {'max_length': '250', 'unique_for_date': "'startdate'"})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'locations.location': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'termine.recurringtermin': {
            'Meta': {'ordering': "['name']"},
            'byweekday': ('models.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'categories': '<< PUT FIELD DEFINITION HERE >>',
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'createdelta': ('models.IntegerField', [], {'default': '14'}),
            'description': ('models.TextField', ['"Text"'], {'blank': 'True'}),
            'duration': ('models.IntegerField', ["'Dauer'"], {'null': 'True', 'blank': 'True'}),
            'first_date': ('models.DateField', [], {}),
            'frequency': ('models.IntegerField', [], {'max_length': '10'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'interval': ('models.IntegerField', [], {'default': '1'}),
            'last_created': ('models.ForeignKey', ['Termin'], {'related_name': '"latest_instance"', 'null': 'True', 'blank': 'True'}),
            'location': ('models.ForeignKey', ['Location'], {'null': 'True', 'verbose_name': '"Ort"', 'blank': 'True'}),
            'modified': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'organizers': '<< PUT FIELD DEFINITION HERE >>',
            'owner': ('models.ForeignKey', ['User'], {'null': 'True', 'blank': 'True'}),
            'rule_description': ('models.CharField', [], {'max_length': '200'}),
            'starttime': ('models.TimeField', ['"Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'summary': ('models.CharField', ['"Titel"'], {'max_length': '250', 'unique_for_date': "'startdate'"})
        },
        'organizers.organizer': {
            'Meta': {'ordering': "['name']"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'termine.category': {
            'Meta': {'ordering': "['name']"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'slug': ('models.SlugField', [], {})
        }
    }
    
    complete_apps = ['termine']
