# Generated by Django 5.0.1 on 2024-02-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_category_description_remove_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена маршрута'),
        ),
    ]
