# Generated by Django 3.0.7 on 2020-07-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20200726_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thesis',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='thesis',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
