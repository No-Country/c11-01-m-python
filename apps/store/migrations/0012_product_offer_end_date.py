# Generated by Django 4.0 on 2023-06-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_options_product_is_offer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
