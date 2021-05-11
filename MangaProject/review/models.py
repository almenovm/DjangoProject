import datetime
from django.db import models
from utils.constants import RATING_CHOICES
from auth_.models import MainUser
# Create your models here.


class Comment(models.Model):
    main_user = models.ForeignKey(MainUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст', null=True)
    created_date = models.DateField(verbose_name='Дата создания', default=datetime.date.today)

    class Meta:
        abstract = True

class Review(Comment):
    title = models.CharField(max_length=255, verbose_name='Тема')
    rating = models.PositiveIntegerField('Рейтинг товара', choices=RATING_CHOICES, default='0/5 - оценок пока нет')

class Reply(Comment):
    review = models.ForeignKey(Review, verbose_name='Отзыв', on_delete=models.CASCADE)