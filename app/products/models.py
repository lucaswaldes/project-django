from django.db import models

from base.models import BaseModel, SoftDelete

class Product(SoftDelete):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	price = models.IntegerField()

	class Meta:
		db_table = 'products'
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'

	def __str__(self):
		return str(self.title)
