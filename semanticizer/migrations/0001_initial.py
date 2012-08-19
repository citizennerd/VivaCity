# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataSetFormat'
        db.create_table('semanticizer_datasetformat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('module', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geographic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('configuration_requirements', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('semanticizer', ['DataSetFormat'])

        # Adding model 'DataSet'
        db.create_table('semanticizer_dataset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semanticizer.DataSetFormat'])),
            ('format_configuration', self.gf('django.db.models.fields.TextField')()),
            ('refresh_period', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('semanticizer', ['DataSet'])

        # Adding model 'Semantics'
        db.create_table('semanticizer_semantics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='semantics', to=orm['semanticizer.DataSet'])),
            ('data_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['postdoc.DataModel'])),
        ))
        db.send_create_signal('semanticizer', ['Semantics'])

        # Adding model 'SemanticsSpecification'
        db.create_table('semanticizer_semanticsspecification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('semantics', self.gf('django.db.models.fields.related.ForeignKey')(related_name='associations', to=orm['semanticizer.Semantics'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['postdoc.DataModelAttribute'])),
            ('column', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('column_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('data_transformation', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('semanticizer', ['SemanticsSpecification'])

        # Adding model 'GeoSemanticsSpecification'
        db.create_table('semanticizer_geosemanticsspecification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('semantics', self.gf('django.db.models.fields.related.ForeignKey')(related_name='geo_associations', to=orm['semanticizer.Semantics'])),
            ('column', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('column_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_geo_x', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_geo_y', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_transformation', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('semanticizer', ['GeoSemanticsSpecification'])

    def backwards(self, orm):
        # Deleting model 'DataSetFormat'
        db.delete_table('semanticizer_datasetformat')

        # Deleting model 'DataSet'
        db.delete_table('semanticizer_dataset')

        # Deleting model 'Semantics'
        db.delete_table('semanticizer_semantics')

        # Deleting model 'SemanticsSpecification'
        db.delete_table('semanticizer_semanticsspecification')

        # Deleting model 'GeoSemanticsSpecification'
        db.delete_table('semanticizer_geosemanticsspecification')

    models = {
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
        'semanticizer.dataset': {
            'Meta': {'object_name': 'DataSet'},
            'file': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['semanticizer.DataSetFormat']"}),
            'format_configuration': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'refresh_period': ('django.db.models.fields.TextField', [], {})
        },
        'semanticizer.datasetformat': {
            'Meta': {'object_name': 'DataSetFormat'},
            'configuration_requirements': ('django.db.models.fields.TextField', [], {}),
            'geographic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'semanticizer.geosemanticsspecification': {
            'Meta': {'object_name': 'GeoSemanticsSpecification'},
            'column': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'column_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'data_transformation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_geo_x': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_geo_y': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'semantics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'geo_associations'", 'to': "orm['semanticizer.Semantics']"})
        },
        'semanticizer.semantics': {
            'Meta': {'object_name': 'Semantics'},
            'data_model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postdoc.DataModel']"}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'semantics'", 'to': "orm['semanticizer.DataSet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'semanticizer.semanticsspecification': {
            'Meta': {'object_name': 'SemanticsSpecification'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postdoc.DataModelAttribute']"}),
            'column': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'column_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'data_transformation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semantics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'associations'", 'to': "orm['semanticizer.Semantics']"})
        }
    }

    complete_apps = ['semanticizer']