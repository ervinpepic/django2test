from django.db import models

# Create your models here.

class Product(models.Model):
	title 		= models.CharField(max_length=70)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary 	= models.TextField(blank=False, null=False)
	featured	= models.BooleanField()

	def __str__(self):
		return self.title