# Generated by Django 3.1.7 on 2021-05-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210513_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='authors',
            field=models.ManyToManyField(to='main.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='ranobe',
            name='authors',
            field=models.ManyToManyField(to='main.Author', verbose_name='Автор'),
        ),
    ]