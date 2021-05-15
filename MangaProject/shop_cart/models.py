from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from auth_.models import MainUser
from main.models import Manga, Ranobe

# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

class ShopCartItems(models.Model):
    cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Manga,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'