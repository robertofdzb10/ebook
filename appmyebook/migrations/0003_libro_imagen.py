# Generated by Django 4.2.7 on 2023-11-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmyebook', '0002_remove_libro_reseñas_alter_libro_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/libros/'),
        ),
    ]
