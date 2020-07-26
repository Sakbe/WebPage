# Generated by Django 3.0.7 on 2020-07-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20200724_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pubfile',
            field=models.FileField(null=True, upload_to='publications/'),
        ),
    ]
