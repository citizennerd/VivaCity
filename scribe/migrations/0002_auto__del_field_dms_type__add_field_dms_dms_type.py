# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DMS.type'
        db.delete_column('scribe_dms', 'type')

        # Adding field 'DMS.dms_type'
        db.add_column('scribe_dms', 'dms_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['scribe.DMSType']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DMS.type'
        db.add_column('scribe_dms', 'type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250),
                      keep_default=False)

        # Deleting field 'DMS.dms_type'
        db.delete_column('scribe_dms', 'dms_type_id')


    models = {
        'scribe.dms': {
            'API_Key': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DMS'},
            'base_address': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'dms_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scribe.DMSType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'scribe.dmstype': {
            'Meta': {'object_name': 'DMSType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['scribe']