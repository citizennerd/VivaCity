# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataModel'
        db.create_table('postdoc_datamodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('super', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['postdoc.DataModel'], null=True, blank=True)),
            ('is_base', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('geo_representation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contains', null=True, to=orm['postdoc.DataModel'])),
            ('concept', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('postdoc', ['DataModel'])

        # Adding model 'DataTag'
        db.create_table('postdoc_datatag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('super', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='subtags', null=True, to=orm['postdoc.DataTag'])),
        ))
        db.send_create_signal('postdoc', ['DataTag'])

        # Adding model 'ModelTags'
        db.create_table('postdoc_modeltags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags', to=orm['postdoc.DataModel'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='models', to=orm['postdoc.DataTag'])),
        ))
        db.send_create_signal('postdoc', ['ModelTags'])

        # Adding model 'DataModelAttribute'
        db.create_table('postdoc_datamodelattribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attributes', to=orm['postdoc.DataModel'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('data_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['postdoc.DataModel'])),
        ))
        db.send_create_signal('postdoc', ['DataModelAttribute'])

        # Adding model 'DataInstance'
        db.create_table('postdoc_datainstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['postdoc.DataModel'])),
        ))
        db.send_create_signal('postdoc', ['DataInstance'])

        # Adding model 'DataInstanceAttribute'
        db.create_table('postdoc_datainstanceattribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instance', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attributes', to=orm['postdoc.DataInstance'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['postdoc.DataModelAttribute'])),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('postdoc', ['DataInstanceAttribute'])

    def backwards(self, orm):
        # Deleting model 'DataModel'
        db.delete_table('postdoc_datamodel')

        # Deleting model 'DataTag'
        db.delete_table('postdoc_datatag')

        # Deleting model 'ModelTags'
        db.delete_table('postdoc_modeltags')

        # Deleting model 'DataModelAttribute'
        db.delete_table('postdoc_datamodelattribute')

        # Deleting model 'DataInstance'
        db.delete_table('postdoc_datainstance')

        # Deleting model 'DataInstanceAttribute'
        db.delete_table('postdoc_datainstanceattribute')

    models = {
        'postdoc.datainstance': {
            'Meta': {'object_name': 'DataInstance'},
            'data_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['postdoc.DataModel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'postdoc.datainstanceattribute': {
            'Meta': {'object_name': 'DataInstanceAttribute'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postdoc.DataModelAttribute']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attributes'", 'to': "orm['postdoc.DataInstance']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'postdoc.datamodel': {
            'Meta': {'object_name': 'DataModel'},
            'concept': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'container': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contains'", 'null': 'True', 'to': "orm['postdoc.DataModel']"}),
            'geo_representation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_base': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'super': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postdoc.DataModel']", 'null': 'True', 'blank': 'True'})
        },
        'postdoc.datamodelattribute': {
            'Meta': {'object_name': 'DataModelAttribute'},
            'data_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postdoc.DataModel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attributes'", 'to': "orm['postdoc.DataModel']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'postdoc.datatag': {
            'Meta': {'object_name': 'DataTag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'super': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subtags'", 'null': 'True', 'to': "orm['postdoc.DataTag']"})
        },
        'postdoc.modeltags': {
            'Meta': {'object_name': 'ModelTags'},
            'data_model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': "orm['postdoc.DataModel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'models'", 'to': "orm['postdoc.DataTag']"})
        }
    }

    complete_apps = ['postdoc']