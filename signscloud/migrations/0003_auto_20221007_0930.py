# Generated by Django 3.2.8 on 2022-10-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signscloud', '0002_brands_deals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='logo',
            field=models.ImageField(blank='', default='', upload_to='Photos/'),
        ),
        migrations.AlterField(
            model_name='deals',
            name='image',
            field=models.ImageField(blank='', default='', upload_to='imagenes/'),
        ),
    ]
