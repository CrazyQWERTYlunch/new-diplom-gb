# Generated by Django 5.0.1 on 2024-02-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(default='Предстоит', max_length=10, verbose_name='Статус события'),
        ),
    ]
