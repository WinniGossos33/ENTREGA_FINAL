# Generated by Django 4.1.1 on 2022-09-29 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0002_alter_avatar_imagen_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='paquete_turistico',
        ),
    ]
