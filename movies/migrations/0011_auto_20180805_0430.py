# Generated by Django 2.1 on 2018-08-05 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20180805_0409'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Migration',
            new_name='Subscription',
        ),
        migrations.AlterModelTable(
            name='subscription',
            table='subscriptions',
        ),
    ]