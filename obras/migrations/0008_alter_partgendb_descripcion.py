# Generated by Django 5.0.1 on 2024-02-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0007_alter_fase_id_obra_alter_partresult_id_obra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partgendb',
            name='descripcion',
            field=models.TextField(max_length=400),
        ),
    ]