from django.db import models
from photologue.models import Gallery
# Create your models here.
class Photographer(models.Model):
	name = models.CharField(max_length=25)
	pgr_avatar = models.ImageField(upload_to = '/media/avatar/', default = '/media/photo.jpg')
	location = models.CharField(max_length=25)
	gallery = models.OneToOneField(Gallery, null = True )

	class Meta:
		db_table = 'photographers'

	def __unicode__(self):
		return self.name

