# Generated by Django 4.0 on 2023-05-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_product',
            field=models.IntegerField(),
        ),
    ]
