# Generated by Django 2.2.5 on 2020-02-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('age', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
