# Generated by Django 3.0.7 on 2020-07-26 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_auto_20200726_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thesis',
            old_name='body',
            new_name='title',
        ),
    ]
