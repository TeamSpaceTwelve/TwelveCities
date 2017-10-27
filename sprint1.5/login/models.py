from django.db import models

# Create your models here.

options = (
	('0','Student'),
	('1','Tourist'),
	('2','Business'),
	('3','Admin'),
)

class account(models.Model):
	username = models.CharField(primary_key = 'true', max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	type = models.CharField(max_length=1, choices = options)
	def __str__(self):
                return self.username
	
