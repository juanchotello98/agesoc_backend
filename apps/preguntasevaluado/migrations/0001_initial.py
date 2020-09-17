# Generated by Django 3.1.1 on 2020-09-17 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pregunta', '0001_initial'),
        ('respuesta', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntasevaluado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas_evaluado', to=settings.AUTH_USER_MODEL)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas_evaluado', to='pregunta.pregunta')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas_evaluado', to='respuesta.respuesta')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]