# Generated by Django 2.1.2 on 2018-11-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181107_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='rut',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
