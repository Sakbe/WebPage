# Generated by Django 3.0.7 on 2020-07-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_auto_20200726_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='techs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
