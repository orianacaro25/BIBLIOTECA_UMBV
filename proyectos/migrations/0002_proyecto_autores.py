# Generated by Django 5.2.3 on 2025-06-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='autores',
            field=models.TextField(blank=True, null=True),
        ),
    ]
