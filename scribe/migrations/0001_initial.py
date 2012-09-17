# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DMS'
        db.create_table('scribe_dms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('base_address', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('API_Key', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('scribe', ['DMS'])

        # Adding model 'DMSType'
        db.create_table('scribe_dmstype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('module', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('scribe', ['DMSType'])


    def backwards(self, orm):
        # Deleting model 'DMS'
        db.delete_table('scribe_dms')

        # Deleting model 'DMSType'
        db.delete_table('scribe_dmstype')


    models = {
        'scribe.dms': {
            'API_Key': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DMS'},
            'base_address': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'scribe.dmstype': {
            'Meta': {'object_name': 'DMSType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['scribe']