# Generated by Django 2.2.5 on 2020-02-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=21, max_length=264, unique=True),
            preserve_default=False,
        ),
    ]
