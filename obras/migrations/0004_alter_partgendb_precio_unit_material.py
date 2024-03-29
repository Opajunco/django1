# Generated by Django 5.0.1 on 2024-02-25 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0003_alter_partresult_empr_alter_partresult_fase_and_more'),
        ('user', '0010_rename_id_org_employee_org_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partgendb',
            name='precio_unit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('comments', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.DateTimeField(auto_now=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.org')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.unit')),
            ],
        ),
    ]
