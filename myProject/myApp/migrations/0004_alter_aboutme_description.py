# Generated by Django 3.2.1 on 2024-09-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
