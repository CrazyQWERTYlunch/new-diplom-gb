# Generated by Django 5.0.1 on 2024-02-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_event_category_alter_event_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='remaining_seats',
            field=models.PositiveIntegerField(default=0, verbose_name='Осталось мест'),
        ),
        migrations.AlterField(
            model_name='event',
            name='total_seats',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Всего мест'),
        ),
    ]
