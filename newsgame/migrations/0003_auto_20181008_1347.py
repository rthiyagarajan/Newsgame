# Generated by Django 2.1.2 on 2018-10-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsgame', '0002_auto_20181008_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]