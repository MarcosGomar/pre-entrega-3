# Generated by Django 4.1.7 on 2023-04-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola_mundo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('raza', models.TextField(max_length=100)),
                ('adoptado', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('apellido', models.TextField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='nombre',
        ),
    ]