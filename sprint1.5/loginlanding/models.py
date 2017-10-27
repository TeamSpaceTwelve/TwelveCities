from django.db import models

class facilities(models.Model):
	email = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	facilityType = models.CharField(max_length=200)
	phone = models.CharField(max_length=10)
	description = models.TextField
	latitude = models.DecimalField(max_digits=8, decimal_places=4)
	longitude = models.DecimalField(max_digits=8, decimal_places=4)
	def __str__(self):
                return self.name
