from django.db import models

# Create your models here.
from utils.validators import validate_size, validate_extension

class AdvsManager(models.Manager):

    def get_by_advs_without_relation(self, advertising_id):
        return self.filter(advertising_id=advertising_id)


class Advertising(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название компании')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='advertising_photos',
                              validators=[validate_size, validate_extension],
                              null=True, blank=True)
    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'

    objects = AdvsManager()


