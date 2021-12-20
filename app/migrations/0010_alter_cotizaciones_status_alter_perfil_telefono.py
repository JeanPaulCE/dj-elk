# Generated by Django 4.0 on 2021-12-20 02:09

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cotizaciones_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
