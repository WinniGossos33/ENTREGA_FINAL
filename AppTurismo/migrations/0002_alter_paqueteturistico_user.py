# Generated by Django 4.1.1 on 2022-10-01 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppTurismo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paqueteturistico',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paquetes', to=settings.AUTH_USER_MODEL),
        ),
    ]
