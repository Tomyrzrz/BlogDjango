# Generated by Django 2.2.9 on 2020-01-27 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20200127_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
    ]
