# Generated by Django 4.1.3 on 2022-12-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0007_alter_alumnos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='rut',
            field=models.CharField(max_length=20),
        ),
    ]
