from django.db import models
from utils.constants import M_TYPE_CHOICES, R_TYPE_CHOICES, COLOR_CHOICES

#


class Publisher(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name


class JournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    genre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Жанр')
    publication_date = models.DateField(verbose_name='Дата публикации')
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, verbose_name='Издатель', null=True)

    class Meta:
        ordering = ['name']
        abstract = True
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'


class Manga(JournalBase):
    color_type = models.CharField(max_length=20, choices=COLOR_CHOICES, default='Черно-белый', verbose_name='Цвет манги')
    release_type = models.CharField(max_length=20, choices=M_TYPE_CHOICES, default='Еженедельник', verbose_name='Тип издания')
    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'


class Ranobe(JournalBase):
    type = models.CharField(max_length=20, choices=R_TYPE_CHOICES, default='Для детей', verbose_name='Тип')
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')

    class Meta:
        verbose_name = 'Ранобэ'
        verbose_name_plural = 'Ранобэ'
