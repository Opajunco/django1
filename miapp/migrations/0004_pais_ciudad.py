# Generated by Django 5.0.1 on 2024-01-12 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_article_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero_habitantes', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('alcalde', models.CharField(max_length=100)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.pais')),
            ],
            options={
                'db_table': 'ciudad',
            },
        ),
    ]