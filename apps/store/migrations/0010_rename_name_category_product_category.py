# Generated by Django 4.0 on 2023-05-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_name_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name_category',
            new_name='category',
        ),
    ]
