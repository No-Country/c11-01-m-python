# Generated by Django 4.0 on 2023-06-02 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_order_receiver_alter_order_receiver_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zip_code',
        ),
    ]
