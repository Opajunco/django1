# Generated by Django 5.0.1 on 2024-01-18 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0006_user2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User2',
            new_name='User',
        ),
    ]