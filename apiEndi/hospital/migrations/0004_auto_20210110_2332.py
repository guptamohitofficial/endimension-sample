# Generated by Django 3.1.4 on 2021-01-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20210110_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.DateField(null=True),
        ),
    ]
