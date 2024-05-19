# Generated by Django 5.0.5 on 2024-05-19 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_auction.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='category_ky',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_auction.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_auction.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='city_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='city_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='city_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='country_en',
            field=models.CharField(max_length=32, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='car',
            name='country_ky',
            field=models.CharField(max_length=32, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='car',
            name='country_ru',
            field=models.CharField(max_length=32, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='car',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]