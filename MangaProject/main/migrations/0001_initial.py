# Generated by Django 3.1.7 on 2021-05-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('genre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Жанр')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('publisher', models.CharField(blank=True, max_length=255, null=True, verbose_name='Издатель')),
                ('color_type', models.CharField(choices=[('Черно-белый', 'Черно-белый'), ('Цветной', 'Цветной')], default='Черно-белый', max_length=20, verbose_name='Цвет манги')),
                ('release_type', models.CharField(choices=[('Еженедельник', 'Еженедельник'), ('Ежемесячник', 'Ежемесячник')], default='Еженедельник', max_length=20, verbose_name='Тип издания')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манга',
            },
        ),
        migrations.CreateModel(
            name='Ranobe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('genre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Жанр')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('publisher', models.CharField(blank=True, max_length=255, null=True, verbose_name='Издатель')),
                ('type', models.CharField(choices=[('Для детей', 'Для детей'), ('18+', '18+'), ('16+', '16+')], default='Для детей', max_length=20, verbose_name='Тип')),
                ('num_pages', models.IntegerField(default=0, verbose_name='Количество страниц')),
            ],
            options={
                'verbose_name': 'Ранобэ',
                'verbose_name_plural': 'Ранобэ',
            },
        ),
    ]
