# Generated by Django 2.1.2 on 2018-11-08 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181108_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='tipousuario',
        ),
    ]
