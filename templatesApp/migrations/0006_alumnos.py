# Generated by Django 4.1.3 on 2022-12-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0005_remove_apoderado_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('rut', models.IntegerField(max_length=20)),
                ('edad', models.IntegerField(max_length=10)),
                ('curso', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=40)),
                ('apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templatesApp.apoderado')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templatesApp.profesor')),
            ],
        ),
    ]