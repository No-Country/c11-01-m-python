# Generated by Django 4.0 on 2023-05-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(default='111-111-1111', max_length=25),
        ),
    ]