# Generated by Django 2.2.5 on 2020-02-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0003_auto_20200218_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=128),
        ),
    ]
