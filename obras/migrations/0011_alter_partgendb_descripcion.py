# Generated by Django 5.0.1 on 2024-02-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0010_alter_partgendb_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partgendb',
            name='descripcion',
            field=models.TextField(max_length=600),
        ),
    ]
