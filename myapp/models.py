from django.db import models

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=1500)
	number=models.CharField(max_length=1500)
	def __unicode__(self):
		return self.name
