# Generated by Django 3.1.1 on 2020-09-25 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0002_auto_20200917_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rol',
            old_name='nombre',
            new_name='rol',
        ),
    ]
