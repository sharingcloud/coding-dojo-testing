# Generated by Django 2.1.4 on 2019-03-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
