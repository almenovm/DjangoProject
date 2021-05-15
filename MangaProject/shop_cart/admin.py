from django.contrib import admin

# Register your models here.
from shop_cart.models import ShopCart, ShopCartItems

admin.site.register(ShopCart)
admin.site.register(ShopCartItems)

