# Generated by Django 4.2.2 on 2023-07-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_usuariocliente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocliente',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='usuariocliente',
            name='nombre',
            field=models.CharField(max_length=15, null=True),
        ),
    ]