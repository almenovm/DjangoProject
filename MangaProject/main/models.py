from django.db import models
from rest_framework import serializers

from utils.constants import M_TYPE_CHOICES, R_TYPE_CHOICES, COLOR_CHOICES
import datetime

#
from utils.validators import validate_size, validate_extension



class JournalManager(models.Manager):

    def get_by_author_with_relation(self, author_id):
        return self.get_related().filter(author_id=author_id)

    def get_by_author_without_relation(self, author_id):
        return self.filter(author_id=author_id)

    def get_related(self):
        return self.select_related('authors', 'publisher')



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

class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class JournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    genre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Жанр')
    publication_date = models.DateField(verbose_name='Дата публикации', default=datetime.date.today)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, verbose_name='Издатель', null=True)
    image = models.ImageField(upload_to='journal_photos',
                              validators=[validate_size, validate_extension],
                              null=True, blank=True)

    class Meta:
        ordering = ['name']
        abstract = True
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

    def price_range_validation(value):
        if not (0 <= value <= 30000):
            raise serializers.ValidationError('Invalid price value')


class Manga(JournalBase):
    color_type = models.CharField(max_length=20, choices=COLOR_CHOICES, default='Черно-белый', verbose_name='Цвет манги')
    release_type = models.CharField(max_length=20, choices=M_TYPE_CHOICES, default='Еженедельник', verbose_name='Тип издания')
    objects = JournalManager()
    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'




class Ranobe(JournalBase):
    type = models.CharField(max_length=20, choices=R_TYPE_CHOICES, default='Для детей', verbose_name='Тип')
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')

    class Meta:
        verbose_name = 'Ранобэ'
        verbose_name_plural = 'Ранобэ'

    def num_pages_range_validation(value):
        if not (1 <= value <= 1700):
            raise serializers.ValidationError('Invalid num_pages value')

class SemilarManga(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, null=True)

class SemilarRanobe(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    ranobe = models.ForeignKey(Ranobe, on_delete=models.CASCADE, null=True)

