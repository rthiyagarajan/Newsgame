# Generated by Django 2.1.2 on 2018-10-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsgame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='entity',
            field=models.ManyToManyField(blank=True, to='newsgame.Entity'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='qnas',
            field=models.ManyToManyField(blank=True, to='newsgame.QNA'),
        ),
    ]