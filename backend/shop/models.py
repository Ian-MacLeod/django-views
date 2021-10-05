from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=256, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    count = models.IntegerField()

    class Meta:
        unique_together = [
            ['shopping_cart', 'item'],
        ]
