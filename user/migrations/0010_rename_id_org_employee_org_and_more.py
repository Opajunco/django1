# Generated by Django 5.0.1 on 2024-02-07 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_employee_id_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='id_org',
            new_name='org',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='id_user',
            new_name='user',
        ),
    ]
