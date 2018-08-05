# Generated by Django 2.1 on 2018-08-05 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Migration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=25, null=True)),
                ('amount', models.IntegerField()),
                ('card_id_number', models.IntegerField()),
                ('expiration_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.User')),
            ],
        ),
    ]
