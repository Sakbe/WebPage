# Generated by Django 3.0.7 on 2020-07-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20200724_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
