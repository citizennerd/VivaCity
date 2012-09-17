# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DSFAlias'
        db.create_table('semanticizer_dsfalias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('dsf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semanticizer.DataSetFormat'])),
        ))
        db.send_create_signal('semanticizer', ['DSFAlias'])


        # Changing field 'DataSet.format_configuration'
        db.alter_column('semanticizer_dataset', 'format_configuration', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DataSet.format'
        db.alter_column('semanticizer_dataset', 'format_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semanticizer.DataSetFormat'], null=True))

    def backwards(self, orm):
        # Deleting model 'DSFAlias'
        db.delete_table('semanticizer_dsfalias')


        # Changing field 'DataSet.format_configuration'
        db.alter_column('semanticizer_dataset', 'format_configuration', self.gf('django.db.models.fields.TextField')(default='\xe2\x88\x9e}{}'))

        # Changing field 'DataSet.format'
        db.alter_column('semanticizer_dataset', 'format_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['semanticizer.DataSetFormat']))

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
            'format': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['semanticizer.DataSetFormat']", 'null': 'True', 'blank': 'True'}),
            'format_configuration': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['semanticizer']