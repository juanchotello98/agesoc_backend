# Generated by Django 3.1.1 on 2020-09-25 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0003_auto_20200916_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proceso',
            old_name='nombre',
            new_name='proceso',
        ),
    ]
