# Generated by Django 4.1.3 on 2022-12-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('rut', models.CharField(max_length=20)),
                ('edad', models.CharField(max_length=40)),
                ('telefono', models.IntegerField(max_length=15)),
                ('SegundoApoderado', models.CharField(max_length=40)),
                ('telefono2', models.IntegerField(max_length=15)),
            ],
        ),
    ]
