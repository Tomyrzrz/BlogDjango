# Generated by Django 2.2.9 on 2020-03-02 18:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20200127_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='detalles',
            field=ckeditor.fields.RichTextField(),
        ),
    ]