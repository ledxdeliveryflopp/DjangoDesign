# Generated by Django 3.2.15 on 2022-11-17 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20221117_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 17, 17, 19, 0, 817153), null=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='name',
            field=models.CharField(error_messages={'unique': 'Такая заявка уже существует!'}, help_text='название', max_length=30, unique=True, verbose_name='Название'),
        ),
    ]
