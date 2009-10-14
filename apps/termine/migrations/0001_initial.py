
from south.db import db
from django.db import models
from termine.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'RecurringTermin'
        db.create_table('termine_recurringtermin', (
            ('id', orm['termine.RecurringTermin:id']),
            ('starttime', orm['termine.RecurringTermin:starttime']),
            ('summary', orm['termine.RecurringTermin:summary']),
            ('description', orm['termine.RecurringTermin:description']),
            ('location', orm['termine.RecurringTermin:location']),
            ('owner', orm['termine.RecurringTermin:owner']),
            ('created', orm['termine.RecurringTermin:created']),
            ('modified', orm['termine.RecurringTermin:modified']),
            ('name', orm['termine.RecurringTermin:name']),
            ('rule_description', orm['termine.RecurringTermin:rule_description']),
            ('weekday', orm['termine.RecurringTermin:weekday']),
            ('frequency', orm['termine.RecurringTermin:frequency']),
            ('first_date', orm['termine.RecurringTermin:first_date']),
            ('interval', orm['termine.RecurringTermin:interval']),
            ('byweekday', orm['termine.RecurringTermin:byweekday']),
            ('duration', orm['termine.RecurringTermin:duration']),
            ('createdelta', orm['termine.RecurringTermin:createdelta']),
            ('last_created', orm['termine.RecurringTermin:last_created']),
        ))
        db.send_create_signal('termine', ['RecurringTermin'])
        
        # Adding model 'Termin'
        db.create_table('termine_termin', (
            ('id', orm['termine.Termin:id']),
            ('starttime', orm['termine.Termin:starttime']),
            ('summary', orm['termine.Termin:summary']),
            ('description', orm['termine.Termin:description']),
            ('location', orm['termine.Termin:location']),
            ('owner', orm['termine.Termin:owner']),
            ('created', orm['termine.Termin:created']),
            ('modified', orm['termine.Termin:modified']),
            ('startdate', orm['termine.Termin:startdate']),
            ('enddate', orm['termine.Termin:enddate']),
            ('slug', orm['termine.Termin:slug']),
            ('rule', orm['termine.Termin:rule']),
            ('publish', orm['termine.Termin:publish']),
        ))
        db.send_create_signal('termine', ['Termin'])
        
        # Adding model 'Category'
        db.create_table('termine_category', (
            ('id', orm['termine.Category:id']),
            ('name', orm['termine.Category:name']),
            ('slug', orm['termine.Category:slug']),
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
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        'organizers.organizer': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'termine.category': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'termine.recurringtermin': {
            'byweekday': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['termine.Category']", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'createdelta': ('django.db.models.fields.IntegerField', [], {'default': '14'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_date': ('django.db.models.fields.DateField', [], {}),
            'frequency': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'last_created': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'latest_instance'", 'blank': 'True', 'null': 'True', 'to': "orm['termine.Termin']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organizers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['organizers.Organizer']", 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'rule_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'starttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'weekday': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'termine.termin': {
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['termine.Category']", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'organizers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['organizers.Organizer']", 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'blank': 'True', 'null': 'True', 'to': "orm['termine.RecurringTermin']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {}),
            'starttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }
    
    complete_apps = ['termine']
