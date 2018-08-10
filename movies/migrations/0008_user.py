# Generated by Django 2.1 on 2018-08-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20180805_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('type', models.CharField(default='FREE', max_length=200)),
                ('password', models.CharField(max_length=25, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
