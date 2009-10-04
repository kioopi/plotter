
from south.db import db
from django.db import models
from termine.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'RecurringTermin.weekday'
        db.add_column('termine_recurringtermin', 'weekday', orm['termine.recurringtermin:weekday'])
        
        # Changing field 'Termin.startdate'
        # (to signature: django.db.models.fields.DateField())
        db.alter_column('termine_termin', 'startdate', orm['termine.termin:startdate'])
        
        # Changing field 'Termin.enddate'
        # (to signature: django.db.models.fields.DateTimeField(null=True, blank=True))
        db.alter_column('termine_termin', 'enddate', orm['termine.termin:enddate'])
        
        # Changing field 'Termin.description'
        # (to signature: django.db.models.fields.TextField(blank=True))
        db.alter_column('termine_termin', 'description', orm['termine.termin:description'])
        
        # Changing field 'Termin.created'
        # (to signature: django.db.models.fields.DateTimeField(auto_now_add=True, blank=True))
        db.alter_column('termine_termin', 'created', orm['termine.termin:created'])
        
        # Changing field 'Termin.modified'
        # (to signature: django.db.models.fields.DateTimeField(auto_now=True, blank=True))
        db.alter_column('termine_termin', 'modified', orm['termine.termin:modified'])
        
        # Changing field 'Termin.rule'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['termine.RecurringTermin']))
        db.alter_column('termine_termin', 'rule_id', orm['termine.termin:rule'])
        
        # Changing field 'Termin.summary'
        # (to signature: django.db.models.fields.CharField(max_length=250))
        db.alter_column('termine_termin', 'summary', orm['termine.termin:summary'])
        
        # Changing field 'Termin.publish'
        # (to signature: django.db.models.fields.BooleanField(default=True, blank=True))
        db.alter_column('termine_termin', 'publish', orm['termine.termin:publish'])
        
        # Changing field 'Termin.starttime'
        # (to signature: django.db.models.fields.TimeField(null=True, blank=True))
        db.alter_column('termine_termin', 'starttime', orm['termine.termin:starttime'])
        
        # Changing field 'Termin.owner'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['auth.User'], null=True, blank=True))
        db.alter_column('termine_termin', 'owner_id', orm['termine.termin:owner'])
        
        # Changing field 'Termin.slug'
        # (to signature: django.db.models.fields.SlugField(max_length=50, db_index=True))
        db.alter_column('termine_termin', 'slug', orm['termine.termin:slug'])
        
        # Changing field 'Termin.location'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['locations.Location'], null=True, blank=True))
        db.alter_column('termine_termin', 'location_id', orm['termine.termin:location'])
        
        # Changing field 'Category.slug'
        # (to signature: django.db.models.fields.SlugField(max_length=50, db_index=True))
        db.alter_column('termine_category', 'slug', orm['termine.category:slug'])
        
        # Changing field 'RecurringTermin.description'
        # (to signature: django.db.models.fields.TextField(blank=True))
        db.alter_column('termine_recurringtermin', 'description', orm['termine.recurringtermin:description'])
        
        # Changing field 'RecurringTermin.created'
        # (to signature: django.db.models.fields.DateTimeField(auto_now_add=True, blank=True))
        db.alter_column('termine_recurringtermin', 'created', orm['termine.recurringtermin:created'])
        
        # Changing field 'RecurringTermin.duration'
        # (to signature: django.db.models.fields.IntegerField(null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'duration', orm['termine.recurringtermin:duration'])
        
        # Changing field 'RecurringTermin.modified'
        # (to signature: django.db.models.fields.DateTimeField(auto_now=True, blank=True))
        db.alter_column('termine_recurringtermin', 'modified', orm['termine.recurringtermin:modified'])
        
        # Changing field 'RecurringTermin.last_created'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['termine.Termin']))
        db.alter_column('termine_recurringtermin', 'last_created_id', orm['termine.recurringtermin:last_created'])
        
        # Changing field 'RecurringTermin.owner'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['auth.User'], null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'owner_id', orm['termine.recurringtermin:owner'])
        
        # Changing field 'RecurringTermin.location'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['locations.Location'], null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'location_id', orm['termine.recurringtermin:location'])
        
        # Changing field 'RecurringTermin.starttime'
        # (to signature: django.db.models.fields.TimeField(null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'starttime', orm['termine.recurringtermin:starttime'])
        
        # Changing field 'RecurringTermin.summary'
        # (to signature: django.db.models.fields.CharField(max_length=250))
        db.alter_column('termine_recurringtermin', 'summary', orm['termine.recurringtermin:summary'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'RecurringTermin.weekday'
        db.delete_column('termine_recurringtermin', 'weekday')
        
        # Changing field 'Termin.startdate'
        # (to signature: models.DateField("Datum"))
        db.alter_column('termine_termin', 'startdate', orm['termine.termin:startdate'])
        
        # Changing field 'Termin.enddate'
        # (to signature: models.DateTimeField("Enddatum und Uhrzeit", null=True, blank=True))
        db.alter_column('termine_termin', 'enddate', orm['termine.termin:enddate'])
        
        # Changing field 'Termin.description'
        # (to signature: models.TextField("Text", blank=True))
        db.alter_column('termine_termin', 'description', orm['termine.termin:description'])
        
        # Changing field 'Termin.created'
        # (to signature: models.DateTimeField(auto_now_add=True))
        db.alter_column('termine_termin', 'created', orm['termine.termin:created'])
        
        # Changing field 'Termin.modified'
        # (to signature: models.DateTimeField(auto_now=True))
        db.alter_column('termine_termin', 'modified', orm['termine.termin:modified'])
        
        # Changing field 'Termin.rule'
        # (to signature: models.ForeignKey(orm['termine.RecurringTermin'], null=True, blank=True))
        db.alter_column('termine_termin', 'rule_id', orm['termine.termin:rule'])
        
        # Changing field 'Termin.summary'
        # (to signature: models.CharField("Titel", max_length=250, unique_for_date='startdate'))
        db.alter_column('termine_termin', 'summary', orm['termine.termin:summary'])
        
        # Changing field 'Termin.publish'
        # (to signature: models.BooleanField("Veroeffentlichen", default=True))
        db.alter_column('termine_termin', 'publish', orm['termine.termin:publish'])
        
        # Changing field 'Termin.starttime'
        # (to signature: models.TimeField("Uhrzeit", null=True, blank=True))
        db.alter_column('termine_termin', 'starttime', orm['termine.termin:starttime'])
        
        # Changing field 'Termin.owner'
        # (to signature: models.ForeignKey(orm['auth.User'], null=True, blank=True))
        db.alter_column('termine_termin', 'owner_id', orm['termine.termin:owner'])
        
        # Changing field 'Termin.slug'
        # (to signature: models.SlugField(unique_for_date='startdate'))
        db.alter_column('termine_termin', 'slug', orm['termine.termin:slug'])
        
        # Changing field 'Termin.location'
        # (to signature: models.ForeignKey(orm['locations.Location'], null=True, blank=True))
        db.alter_column('termine_termin', 'location_id', orm['termine.termin:location'])
        
        # Changing field 'Category.slug'
        # (to signature: models.SlugField())
        db.alter_column('termine_category', 'slug', orm['termine.category:slug'])
        
        # Changing field 'RecurringTermin.description'
        # (to signature: models.TextField("Text", blank=True))
        db.alter_column('termine_recurringtermin', 'description', orm['termine.recurringtermin:description'])
        
        # Changing field 'RecurringTermin.created'
        # (to signature: models.DateTimeField(auto_now_add=True))
        db.alter_column('termine_recurringtermin', 'created', orm['termine.recurringtermin:created'])
        
        # Changing field 'RecurringTermin.duration'
        # (to signature: models.IntegerField('Dauer', null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'duration', orm['termine.recurringtermin:duration'])
        
        # Changing field 'RecurringTermin.modified'
        # (to signature: models.DateTimeField(auto_now=True))
        db.alter_column('termine_recurringtermin', 'modified', orm['termine.recurringtermin:modified'])
        
        # Changing field 'RecurringTermin.last_created'
        # (to signature: models.ForeignKey(orm['termine.Termin'], null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'last_created_id', orm['termine.recurringtermin:last_created'])
        
        # Changing field 'RecurringTermin.owner'
        # (to signature: models.ForeignKey(orm['auth.User'], null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'owner_id', orm['termine.recurringtermin:owner'])
        
        # Changing field 'RecurringTermin.location'
        # (to signature: models.ForeignKey(orm['locations.Location'], null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'location_id', orm['termine.recurringtermin:location'])
        
        # Changing field 'RecurringTermin.starttime'
        # (to signature: models.TimeField("Uhrzeit", null=True, blank=True))
        db.alter_column('termine_recurringtermin', 'starttime', orm['termine.recurringtermin:starttime'])
        
        # Changing field 'RecurringTermin.summary'
        # (to signature: models.CharField("Titel", max_length=250, unique_for_date='startdate'))
        db.alter_column('termine_recurringtermin', 'summary', orm['termine.recurringtermin:summary'])
        
    
    
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
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
            'weekday': ('django.db.models.fields.IntegerField', [], {})
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
