# Generated by Django 5.0.1 on 2024-02-25 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес почты')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Количество')),
                ('payment_by_card', models.BooleanField(default=False, verbose_name='Оплата картой')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('status', models.CharField(choices=[('Ждет подтверждения', 'Ждет подтверждения'), ('Подтвержден', 'Подтвержден'), ('Выполнен', 'Выполнен'), ('Отменен', 'Отменен')], default='Ждет подтверждения', max_length=18, verbose_name='Статус заказа')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('update_timestamp', models.DateTimeField(auto_now=True, verbose_name='Дата изменения заказа')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.event', verbose_name='Прогулка')),
            ],
            options={
                'verbose_name': 'Заказ\\Прогулки',
                'verbose_name_plural': 'Заказы\\Прогулки',
                'db_table': 'order',
            },
        ),
    ]
