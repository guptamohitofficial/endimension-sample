# Generated by Django 3.1.4 on 2021-01-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20210110_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
