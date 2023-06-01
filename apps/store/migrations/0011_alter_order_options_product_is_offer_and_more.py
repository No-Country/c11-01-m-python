# Generated by Django 4.0 on 2023-06-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_paid_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='product',
            name='is_offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='percent_offer',
            field=models.IntegerField(default=0),
        ),
    ]
