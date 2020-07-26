# Generated by Django 3.0.7 on 2020-07-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_auto_20200726_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['category', '-end_date']},
        ),
        migrations.AddField(
            model_name='education',
            name='category',
            field=models.CharField(choices=[('P', 'Postgraduate Training'), ('S', 'Studies')], default='P', max_length=1),
        ),
    ]