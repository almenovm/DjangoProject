from .models import Advertising
from django.dispatch import  receiver
from django.db.models.signals import post_save, post_delete
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Advertising)
def advs_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('created')
        logger.info('created')
        logger.warning('created')
        logger.error('created')
        logger.critical('created')
