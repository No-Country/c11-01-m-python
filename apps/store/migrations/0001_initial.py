# Generated by Django 4.0 on 2023-05-14 21:36

import apps.helper.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.CharField(default=apps.helper.utilities.pkgen, max_length=6, primary_key=True, serialize=False)),
                ('name_category', models.CharField(max_length=255)),
                ('description_category', models.TextField()),
                ('image_category', models.ImageField(upload_to='Category')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
