# Generated by Django 2.1 on 2018-08-05 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='category_id',
            new_name='category',
        ),
    ]
