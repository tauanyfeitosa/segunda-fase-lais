# Generated by Django 4.1 on 2022-08-15 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansuz', '0003_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='termos_uso',
            field=models.BooleanField(verbose_name='Termos de Uso'),
        ),
    ]
