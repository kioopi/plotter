
from south.db import db
from django.db import models
from termine.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'RecurringTermin'
        db.create_table('termine_recurringtermin', (
            ('id', models.AutoField(primary_key=True)),
            ('starttime', models.TimeField("Uhrzeit", null=True, blank=True)),
            ('summary', models.CharField("Titel", max_length=250, unique_for_date='startdate')),
            ('description', models.TextField("Text", blank=True)),
            ('location', models.ForeignKey(orm['locations.Location'], null=True, blank=True)),
            ('owner', models.ForeignKey(orm['auth.User'], null=True, blank=True)),
            ('created', models.DateTimeField(auto_now_add=True)),
            ('modified', models.DateTimeField(auto_now=True)),
            ('name', models.CharField(max_length=100)),
            ('rule_description', models.CharField(max_length=200)),
            ('frequency', models.IntegerField(max_length=10)),
            ('first_date', models.DateField()),
            ('interval', models.IntegerField(default=1)),
            ('byweekday', models.CharField(max_length=20, blank=True)),
            ('duration', models.IntegerField('Dauer', null=True, blank=True)),
            ('createdelta', models.IntegerField(default=14)),
            ('last_created', models.ForeignKey(orm.Termin, related_name="latest_instance", null=True, blank=True)),
        ))
        db.send_create_signal('termine', ['RecurringTermin'])
        
        # Adding model 'Termin'
        db.create_table('termine_termin', (
            ('id', models.AutoField(primary_key=True)),
            ('starttime', models.TimeField("Uhrzeit", null=True, blank=True)),
            ('summary', models.CharField("Titel", max_length=250, unique_for_date='startdate')),
            ('description', models.TextField("Text", blank=True)),
            ('location', models.ForeignKey(orm['locations.Location'], null=True, blank=True)),
            ('owner', models.ForeignKey(orm['auth.User'], null=True, blank=True)),
            ('created', models.DateTimeField(auto_now_add=True)),
            ('modified', models.DateTimeField(auto_now=True)),
            ('startdate', models.DateField("Datum")),
            ('enddate', models.DateTimeField("Enddatum und Uhrzeit", null=True, blank=True)),
            ('slug', models.SlugField(unique_for_date='startdate')),
            ('rule', models.ForeignKey(orm.RecurringTermin, related_name="instances", null=True, blank=True)),
            ('publish', models.BooleanField("Veroeffentlichen", default=True)),
        ))
        db.send_create_signal('termine', ['Termin'])
        
        # Adding model 'Category'
        db.create_table('termine_category', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
            ('slug', models.SlugField()),
        ))
        db.send_create_signal('termine', ['Category'])
        
        # Adding ManyToManyField 'RecurringTermin.organizers'
        db.create_table('termine_recurringtermin_organizers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recurringtermin', models.ForeignKey(orm.RecurringTermin, null=False)),
            ('organizer', models.ForeignKey(orm['organizers.Organizer'], null=False))
        ))
        
        # Adding ManyToManyField 'Termin.organizers'
        db.create_table('termine_termin_organizers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('termin', models.ForeignKey(orm.Termin, null=False)),
            ('organizer', models.ForeignKey(orm['organizers.Organizer'], null=False))
        ))
        
        # Adding ManyToManyField 'Termin.categories'
        db.create_table('termine_termin_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('termin', models.ForeignKey(orm.Termin, null=False)),
            ('category', models.ForeignKey(orm.Category, null=False))
        ))
        
        # Adding ManyToManyField 'RecurringTermin.categories'
        db.create_table('termine_recurringtermin_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recurringtermin', models.ForeignKey(orm.RecurringTermin, null=False)),
            ('category', models.ForeignKey(orm.Category, null=False))
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
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'organizers.organizer': {
            'Meta': {'ordering': "['name']"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'locations.location': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'termine.termin': {
            'Meta': {'ordering': "['startdate','starttime','location','slug']", 'get_latest_by': "'startdate'"},
            'categories': ('models.ManyToManyField', ["orm['termine.Category']"], {'blank': 'True'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', ['"Text"'], {'blank': 'True'}),
            'enddate': ('models.DateTimeField', ['"Enddatum und Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'location': ('models.ForeignKey', ["orm['locations.Location']"], {'null': 'True', 'blank': 'True'}),
            'modified': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'organizers': ('models.ManyToManyField', ["orm['organizers.Organizer']"], {'blank': 'True'}),
            'owner': ('models.ForeignKey', ["orm['auth.User']"], {'null': 'True', 'blank': 'True'}),
            'publish': ('models.BooleanField', ['"Veroeffentlichen"'], {'default': 'True'}),
            'rule': ('models.ForeignKey', ["orm['termine.RecurringTermin']"], {'related_name': '"instances"', 'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'unique_for_date': "'startdate'"}),
            'startdate': ('models.DateField', ['"Datum"'], {}),
            'starttime': ('models.TimeField', ['"Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'summary': ('models.CharField', ['"Titel"'], {'max_length': '250', 'unique_for_date': "'startdate'"})
        },
        'termine.recurringtermin': {
            'Meta': {'ordering': "['name']"},
            'byweekday': ('models.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'categories': ('models.ManyToManyField', ["orm['termine.Category']"], {'blank': 'True'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'createdelta': ('models.IntegerField', [], {'default': '14'}),
            'description': ('models.TextField', ['"Text"'], {'blank': 'True'}),
            'duration': ('models.IntegerField', ["'Dauer'"], {'null': 'True', 'blank': 'True'}),
            'first_date': ('models.DateField', [], {}),
            'frequency': ('models.IntegerField', [], {'max_length': '10'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'interval': ('models.IntegerField', [], {'default': '1'}),
            'last_created': ('models.ForeignKey', ["orm['termine.Termin']"], {'related_name': '"latest_instance"', 'null': 'True', 'blank': 'True'}),
            'location': ('models.ForeignKey', ["orm['locations.Location']"], {'null': 'True', 'blank': 'True'}),
            'modified': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'organizers': ('models.ManyToManyField', ["orm['organizers.Organizer']"], {'blank': 'True'}),
            'owner': ('models.ForeignKey', ["orm['auth.User']"], {'null': 'True', 'blank': 'True'}),
            'rule_description': ('models.CharField', [], {'max_length': '200'}),
            'starttime': ('models.TimeField', ['"Uhrzeit"'], {'null': 'True', 'blank': 'True'}),
            'summary': ('models.CharField', ['"Titel"'], {'max_length': '250', 'unique_for_date': "'startdate'"})
        },
        'termine.category': {
            'Meta': {'ordering': "['name']"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'}),
            'slug': ('models.SlugField', [], {})
        }
    }
    
    complete_apps = ['termine']
