from .models import Reply, Review
from django.dispatch import  receiver
from django.db.models.signals import post_save, post_delete
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Review)
def review_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('created')
        logger.info('created')
        logger.warning('created')
        logger.error('created')
        logger.critical('created')

@receiver(post_save, sender=Reply)
def reply_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('created')
        logger.info('created')
        logger.warning('created')
        logger.error('created')
        logger.critical('created')

# @receiver(post_delete, sender=Reply)
# def reply_deleted(sender, instance, deleted, **kwargs):
#     if deleted:
#         logger.debug('deleted')
#         logger.info('deleted')
#         logger.warning('deleted')
#         logger.error('deleted')
#         logger.critical('deleted')
#
# @receiver(post_delete, sender=Review)
# def review_deleted(sender, instance, deleted, **kwargs):
#     if deleted:
#         logger.debug('deleted')
#         logger.info('deleted')
#         logger.warning('deleted')
#         logger.error('deleted')
#         logger.critical('deleted')