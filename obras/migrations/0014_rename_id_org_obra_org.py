# Generated by Django 5.0.1 on 2024-02-06 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0013_rename_id_obra_fase_obra_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obra',
            old_name='id_org',
            new_name='org',
        ),
    ]