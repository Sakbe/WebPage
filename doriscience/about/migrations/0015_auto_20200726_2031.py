# Generated by Django 3.0.7 on 2020-07-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_auto_20200726_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='place',
            field=models.CharField(blank=True, default='Thesis Place', max_length=200),
        ),
    ]
