from django.db import models

from base.models import BaseModel, SoftDelete
from products.models import Product
from discord.models import DiscordUser


class Order(SoftDelete):
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE, blank=True, null=True, related_name="user_order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='product_order')
    code = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
	    db_table = 'orders'
	    verbose_name = 'Pedido'
	    verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(f"{self.user} - {self.product}")
