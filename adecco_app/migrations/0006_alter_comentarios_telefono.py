# Generated by Django 4.0.3 on 2022-04-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adecco_app', '0005_alter_comentarios_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='telefono',
            field=models.CharField(max_length=150),
        ),
    ]
