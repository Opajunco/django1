# Generated by Django 5.0.1 on 2024-01-21 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0005_obra_id_org'),
        ('user', '0009_alter_employee_id_org'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ab', models.CharField(max_length=5)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('order', models.IntegerField()),
                ('id_Obra', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
            ],
        ),
        migrations.CreateModel(
            name='PartGenDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unit', models.DecimalField(decimal_places=4, max_digits=12)),
                ('descripcion', models.CharField(max_length=400)),
                ('comentarios', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateTimeField(auto_now=True)),
                ('id_capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.capitulo')),
                ('id_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.org')),
                ('id_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.unit')),
            ],
        ),
        migrations.CreateModel(
            name='PartResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('comments', models.TextField()),
                ('checklater', models.BooleanField(default=False)),
                ('checkdel', models.BooleanField(default=False)),
                ('checkended', models.BooleanField(default=False)),
                ('precio_unit_mod', models.DecimalField(decimal_places=4, max_digits=12)),
                ('cantidad', models.DecimalField(decimal_places=4, max_digits=12)),
                ('id_Obra', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
                ('id_fase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.fase')),
            ],
        ),
        migrations.CreateModel(
            name='PartGen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unit_mod', models.DecimalField(decimal_places=4, max_digits=12)),
                ('cantidad', models.DecimalField(decimal_places=4, max_digits=12)),
                ('id_partgendb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.partgendb')),
                ('id_partresult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.partresult')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('order', models.IntegerField()),
                ('id_Obra', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
            ],
        ),
        migrations.AddField(
            model_name='partresult',
            name='id_zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.zona'),
        ),
    ]