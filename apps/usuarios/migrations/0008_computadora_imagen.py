# Generated by Django 2.2.9 on 2020-03-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20200302_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='computadora',
            name='imagen',
            field=models.URLField(null=True, verbose_name='Imagen'),
        ),
    ]
