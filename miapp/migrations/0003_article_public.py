# Generated by Django 5.0.1 on 2024-01-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='public',
            field=models.BooleanField(default='False'),
        ),
    ]
