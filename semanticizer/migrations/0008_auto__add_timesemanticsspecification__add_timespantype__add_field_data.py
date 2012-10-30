# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimeSemanticsSpecification'
        db.create_table('semanticizer_timesemanticsspecification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('semantics', self.gf('django.db.models.fields.related.ForeignKey')(related_name='time_associations', to=orm['semanticizer.Semantics'])),
            ('column', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data_transformation', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timespan_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semanticizer.TimeSpanType'])),
        ))
        db.send_create_signal('semanticizer', ['TimeSemanticsSpecification'])

        # Adding model 'TimeSpanType'
        db.create_table('semanticizer_timespantype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('semanticizer', ['TimeSpanType'])

        # Adding field 'DataSetFormat.time_explicit'
        db.add_column('semanticizer_datasetformat', 'time_explicit',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'DataSetFormat.time_implicit'
        db.add_column('semanticizer_datasetformat', 'time_implicit',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TimeSemanticsSpecification'
        db.delete_table('semanticizer_timesemanticsspecification')

        # Deleting model 'TimeSpanType'
        db.delete_table('semanticizer_timespantype')

        # Deleting field 'DataSetFormat.time_explicit'
        db.delete_column('semanticizer_datasetformat', 'time_explicit')

        # Deleting field 'DataSetFormat.time_implicit'
        db.delete_column('semanticizer_datasetformat', 'time_implicit')


    models = {
        'postdoc.datamodel': {
            'Meta': {'object_name': 'DataModel'},
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
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['semanticizer.DataSetFormat']", 'null': 'True', 'blank': 'True'}),
            'format_configuration': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publication_aggregation': ('django.db.models.fields.TextField', [], {}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time_explicit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_implicit': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'semanticizer.dsfalias': {
            'Meta': {'object_name': 'DSFAlias'},
            'dsf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['semanticizer.DataSetFormat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'semanticizer.geosemanticsspecification': {
            'Meta': {'object_name': 'GeoSemanticsSpecification'},
            'column': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'data_transformation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geocode_address': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'semantics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'associations'", 'to': "orm['semanticizer.Semantics']"}),
            'via': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'path'", 'null': 'True', 'to': "orm['semanticizer.SemanticsSpecificationPath']"})
        },
        'semanticizer.semanticsspecificationpath': {
            'Meta': {'object_name': 'SemanticsSpecificationPath'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['postdoc.DataModelAttribute']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'previous'", 'null': 'True', 'to': "orm['semanticizer.SemanticsSpecificationPath']"})
        },
        'semanticizer.timesemanticsspecification': {
            'Meta': {'object_name': 'TimeSemanticsSpecification'},
            'column': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'data_transformation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semantics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'time_associations'", 'to': "orm['semanticizer.Semantics']"}),
            'timespan_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['semanticizer.TimeSpanType']"})
        },
        'semanticizer.timespantype': {
            'Meta': {'object_name': 'TimeSpanType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['semanticizer']