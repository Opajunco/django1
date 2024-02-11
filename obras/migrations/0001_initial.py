# Generated by Django 5.0.1 on 2024-02-09 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0010_rename_id_org_employee_org_and_more'),
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
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('concepto', models.CharField(max_length=300)),
                ('comentarios', models.TextField()),
                ('diario', models.TextField()),
                ('porcGg', models.DecimalField(decimal_places=4, max_digits=6)),
                ('porcBi', models.DecimalField(decimal_places=4, max_digits=6)),
                ('gastosFijos', models.DecimalField(decimal_places=4, max_digits=10)),
                ('image', models.ImageField(default='null', upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ended', models.BooleanField(default=False)),
                ('org', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.org')),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField()),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
            ],
        ),
        migrations.CreateModel(
            name='Empr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField()),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
            ],
        ),
        migrations.CreateModel(
            name='PartGenDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unit', models.DecimalField(decimal_places=4, max_digits=12)),
                ('descripcion', models.TextField(max_length=600)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateTimeField(auto_now=True)),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.capitulo')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.org')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.unit')),
            ],
        ),
        migrations.CreateModel(
            name='PartResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('checklater', models.BooleanField(default=False)),
                ('checkdel', models.BooleanField(default=False)),
                ('checkended', models.BooleanField(default=False)),
                ('precio_unit_mod', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('terminado', models.DecimalField(decimal_places=4, default=0, max_digits=5)),
                ('main_coef', models.DecimalField(decimal_places=4, default=1.2, max_digits=5)),
                ('empr_coef', models.DecimalField(decimal_places=4, default=0.8, max_digits=5)),
                ('empr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='obras.empr')),
                ('fase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='obras.fase')),
                ('obra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
            ],
        ),
        migrations.CreateModel(
            name='PartGen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unit_mod', models.DecimalField(decimal_places=4, max_digits=12)),
                ('cantidad', models.DecimalField(decimal_places=4, max_digits=12)),
                ('partgendb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.partgendb')),
                ('partresult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.partresult')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField()),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
            ],
        ),
        migrations.AddField(
            model_name='partresult',
            name='zona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='obras.zona'),
        ),
    ]
