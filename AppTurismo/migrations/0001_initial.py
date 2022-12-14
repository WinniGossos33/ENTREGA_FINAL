# Generated by Django 4.1.1 on 2022-10-02 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=33)),
                ('apellido', models.CharField(max_length=33)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('celular', models.PositiveIntegerField()),
                ('dni', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaqueteTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugares', models.IntegerField(choices=[(1, 'Amsterdam'), (2, 'Rio de Janeiro'), (3, 'Barcelona'), (4, 'Miami'), (5, 'Mendoza'), (6, 'Buenos Aires')], default=1)),
                ('fecha_de_entrada', models.DateField()),
                ('fecha_de_salida', models.DateField()),
                ('empleado_asignado', models.CharField(blank=True, max_length=33, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paquetes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaqueteAcompanante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTurismo.cliente')),
                ('paquete_turistico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTurismo.paqueteturistico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
