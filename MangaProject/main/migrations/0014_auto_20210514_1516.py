# Generated by Django 3.1.7 on 2021-05-14 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210514_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semilarmanga',
            name='manga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.manga'),
        ),
        migrations.AlterField(
            model_name='semilarranobe',
            name='ranobe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ranobe'),
        ),
    ]
