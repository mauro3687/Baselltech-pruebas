# Generated by Django 4.2.2 on 2023-07-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_usuariocliente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocliente',
            name='fecha_nacimiento',
            field=models.DateField(default='YYYY-MM-DD'),
        ),
    ]
