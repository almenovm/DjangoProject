# Generated by Django 3.1.7 on 2021-05-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210513_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='authors',
        ),
        migrations.AddField(
            model_name='manga',
            name='authors',
            field=models.ManyToManyField(to='main.Author'),
        ),
        migrations.RemoveField(
            model_name='ranobe',
            name='authors',
        ),
        migrations.AddField(
            model_name='ranobe',
            name='authors',
            field=models.ManyToManyField(to='main.Author'),
        ),
    ]
