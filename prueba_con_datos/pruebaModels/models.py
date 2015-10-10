from django.db import models

class Coche(models.Model):
	marca = models.CharField(max_length=30)
	modelo = models.TextField()

	def __unicode__(self):
		return self.marca + " " + self.modelo

