# Generated by Django 4.0 on 2023-05-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_product',
            field=models.ImageField(upload_to='media/Items/'),
        ),
    ]
