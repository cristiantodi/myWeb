# Generated by Django 4.1.dev20211123065844 on 2022-08-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_alter_servicio_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.TextField(),
        ),
    ]
