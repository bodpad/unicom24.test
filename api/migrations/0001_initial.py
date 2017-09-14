# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('passport_no', models.CharField(max_length=10, verbose_name='Номер паспорта')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('credit_score', models.IntegerField(verbose_name='Скоринговый балл')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')),
                ('modify_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время изменения')),
            ],
            options={
                'verbose_name': 'Анкета клиента',
                'verbose_name_plural': 'Анкеты клиентов',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название\tпредложения')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Потреб'), (2, 'Ипотека'), (3, 'Аавтокредит'), (4, 'КМСБ')], verbose_name='Тип предложения')),
                ('min_credit_score', models.IntegerField(default=0, verbose_name='Минимальный скоринговый балл')),
                ('max_credit_score', models.IntegerField(default=1000, verbose_name='Максимальный скоринговый балл')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('modify_date', models.DateTimeField(auto_now_add=True)),
                ('rotation_start', models.DateTimeField(verbose_name='Дата и время начала ротации')),
                ('rotation_end', models.DateTimeField(verbose_name='Дата и время окончания ротации')),
                ('credit_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кредитная организация')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
        migrations.CreateModel(
            name='Request2co',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')),
                ('sent_date', models.DateTimeField(auto_now=True, verbose_name='Дата и время отправки')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'NEW'), (2, 'SENT'), (3, 'RECEIVED')], default=1, verbose_name='Статус')),
                ('customer_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CustomerProfile', verbose_name='Анкета клиента')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Offer', verbose_name='Предложение')),
            ],
            options={
                'verbose_name': 'Заявка в кредитную организацию',
                'verbose_name_plural': 'Заявки в кредитные организации',
            },
        ),
    ]