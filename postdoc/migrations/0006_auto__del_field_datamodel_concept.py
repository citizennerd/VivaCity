# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DataModel.concept'
        db.delete_column('postdoc_datamodel', 'concept')


    def backwards(self, orm):
        # Adding field 'DataModel.concept'
        db.add_column('postdoc_datamodel', 'concept',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        'postdoc.datainstance': {
            'Meta': {'object_name': 'DataInstance'},
            'data_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['postdoc.DataModel']"}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryCollectionField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mgeometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'})
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