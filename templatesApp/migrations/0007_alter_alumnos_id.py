# Generated by Django 4.1.3 on 2022-12-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0006_alumnos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]