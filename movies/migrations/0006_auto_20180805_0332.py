# Generated by Django 2.1 on 2018-08-05 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20180805_0309'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='movie',
            table='movie',
        ),
    ]