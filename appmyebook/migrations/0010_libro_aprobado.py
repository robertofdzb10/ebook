# Generated by Django 4.2.7 on 2023-12-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmyebook', '0009_genero_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
    ]