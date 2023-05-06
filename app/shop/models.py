from django.db import models

from base.models import BaseModel, SoftDelete
from products.models import Product
from discord.models import DiscordUser

class Shop(BaseModel):
	user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE, related_name="user_shop", null=True)
	products = models.ManyToManyField(Product, blank=True, related_name='products')

	class Meta:
		db_table = 'shop'
		verbose_name = 'Shop'
		verbose_name_plural = 'Shop'
