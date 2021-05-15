from .models import ShopCart, ShopCartItems
from main.models import Manga
from django.dispatch import receiver
from django.db.models.signals import pre_save
import logging

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=ShopCartItems)
def correct_price(sender, **kwargs):
    logger.debug('corrected')
    logger.info('corrected')
    logger.warning('corrected')
    logger.error('corrected')
    logger.critical('corrected')
    product = Manga
    cart_items = kwargs['instance']
    price_of_product = product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    total_cart_items = ShopCartItems.objects.filter(user = cart_items.user )
    cart = ShopCart.objects.get(id = cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()