# Generated by Django 4.1.dev20211123065844 on 2022-07-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_alter_categoria_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen_categoria',
            field=models.ImageField(blank=True, null=True, upload_to='categoria'),
        ),
    ]
