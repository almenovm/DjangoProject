from django.db import models

# Create your models here.

class JournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    genre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Жанр')
    publication_date = models.DateField(verbose_name='Дата публикации')
    publisher = models.CharField(max_length=255, null=True, blank=True, verbose_name='Издатель')

    class Meta:
        ordering = ['name']
        abstract = True


class Manga(JournalBase):
    color_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Черно-белый', verbose_name='Цвет манги')
    release_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Еженедельник', verbose_name='Тип издания')
    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'


class Ranobe(JournalBase):
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Для детей', verbose_name='Тип')
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')

    class Meta:
        verbose_name = 'Ранобэ'
        verbose_name_plural = 'Ранобэ'
