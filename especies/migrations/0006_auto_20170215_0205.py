# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especies', '0005_auto_20170215_0203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='specie',
            options={'verbose_name': 'Especimen', 'verbose_name_plural': 'Especimenes'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
