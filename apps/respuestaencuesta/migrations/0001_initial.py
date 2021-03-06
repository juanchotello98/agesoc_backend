# Generated by Django 3.1.1 on 2020-09-17 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('respuesta', '0004_auto_20200917_1222'),
        ('proceso', '0003_auto_20200916_1534'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pregunta', '0002_auto_20200917_1222'),
        ('rol', '0002_auto_20200917_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuestaencuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('evaluado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_encuesta', to=settings.AUTH_USER_MODEL)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_encuesta', to='pregunta.pregunta')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_encuesta', to='proceso.proceso')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_encuesta', to='respuesta.respuesta')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_encuesta', to='rol.rol')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
