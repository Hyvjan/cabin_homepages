from __future__ import unicode_literals
from autoslug import AutoSlugField
from django.db import models

# Create your models here.
# Create your models here.
class Reservation(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	arrival_date = models.DateField(auto_now_add=False)
	end_date = models.DateField(auto_now_add=False)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField()
	phone_number = models.CharField(max_length=25)
	message = models.TextField()

	def __unicode__(self):
		return self.last_name

class Pictures(models.Model):
	picture = models.TextField()
	file_up = models.FileField(blank=True)
	url = AutoSlugField(populate_from='picture', editable=True,unique=True, blank=True)

	def __unicode__(self):
		return self.picture

class NaturePictures(models.Model):
	picture_description = models.TextField()
	file_up = models.FileField(blank=True)
	url = AutoSlugField(populate_from='picture_description', editable=True,unique=True, blank=True)

	def __unicode__(self):
		return self.picture_description