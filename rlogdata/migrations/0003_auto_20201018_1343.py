# Generated by Django 3.1 on 2020-10-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlogdata', '0002_auto_20201017_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staging',
            name='DOB',
            field=models.TextField(blank=True, null=True),
        ),
    ]