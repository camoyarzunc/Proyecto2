# Generated by Django 2.1.2 on 2018-11-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_registro_tipousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='correo',
            field=models.CharField(max_length=45),
        ),
    ]
