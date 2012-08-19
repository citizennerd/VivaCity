# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataSetColumn'
        db.create_table('semanticizer_datasetcolumn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='columns', to=orm['semanticizer.DataSet'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('semanticizer', ['DataSetColumn'])

        # Adding unique constraint on 'DataSetColumn', fields ['dataset', 'name']
        db.create_unique('semanticizer_datasetcolumn', ['dataset_id', 'name'])

        # Deleting field 'SemanticsSpecification.column_number'
        db.delete_column('semanticizer_semanticsspecification', 'column_number')


        # Changing field 'SemanticsSpecification.column'
        db.alter_column('semanticizer_semanticsspecification', 'column', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))
        # Adding field 'DataSetFormat.is_api'
        db.add_column('semanticizer_datasetformat', 'is_api',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'DataSet.refresh_period'
        db.alter_column('semanticizer_dataset', 'refresh_period', self.gf('django.db.models.fields.TextField')(null=True))
        # Deleting field 'GeoSemanticsSpecification.column_number'
        db.delete_column('semanticizer_geosemanticsspecification', 'column_number')


        # Changing field 'GeoSemanticsSpecification.column'
        db.alter_column('semanticizer_geosemanticsspecification', 'column', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    def backwards(self, orm):
        # Removing unique constraint on 'DataSetColumn', fields ['dataset', 'name']
        db.delete_unique('semanticizer_datasetcolumn', ['dataset_id', 'name'])

        # Deleting model 'DataSetColumn'
        db.delete_table('semanticizer_datasetcolumn')

        # Adding field 'SemanticsSpecification.column_number'
        db.add_column('semanticizer_semanticsspecification', 'column_number',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'SemanticsSpecification.column'
        db.alter_column('semanticizer_semanticsspecification', 'column', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))
        # Deleting field 'DataSetFormat.is_api'
        db.delete_column('semanticizer_datasetformat', 'is_api')


        # Changing field 'DataSet.refresh_period'
        db.alter_column('semanticizer_dataset', 'refresh_period', self.gf('django.db.models.fields.TextField')(default=None))
        # Adding field 'GeoSemanticsSpecification.column_number'
        db.add_column('semanticizer_geosemanticsspecification', 'column_number',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'GeoSemanticsSpecification.column'
        db.alter_column('semanticizer_geosemanticsspecification', 'column', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

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
            'refresh_period': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'semanticizer.datasetcolumn': {
            'Meta': {'unique_together': "(('dataset', 'name'),)", 'object_name': 'DataSetColumn'},
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'columns'", 'to': "orm['semanticizer.DataSet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'semanticizer.datasetformat': {
            'Meta': {'object_name': 'DataSetFormat'},
            'configuration_requirements': ('django.db.models.fields.TextField', [], {}),
            'geographic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_api': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'semanticizer.geosemanticsspecification': {
            'Meta': {'object_name': 'GeoSemanticsSpecification'},
            'column': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
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
            'column': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'data_transformation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semantics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'associations'", 'to': "orm['semanticizer.Semantics']"})
        }
    }

    complete_apps = ['semanticizer']