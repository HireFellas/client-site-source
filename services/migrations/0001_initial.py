# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photographer'
        db.create_table('photographers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('pgr_avatar', self.gf('django.db.models.fields.files.ImageField')(default='/media/photo.jpg', max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'services', ['Photographer'])


    def backwards(self, orm):
        # Deleting model 'Photographer'
        db.delete_table('photographers')


    models = {
        u'services.photographer': {
            'Meta': {'object_name': 'Photographer', 'db_table': "'photographers'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'pgr_avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/photo.jpg'", 'max_length': '100'})
        }
    }

    complete_apps = ['services']