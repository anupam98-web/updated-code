# Generated by Django 3.1 on 2020-10-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlogdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='badrecords',
            name='month_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='badrecords',
            name='year_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goodrecords',
            name='month_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goodrecords',
            name='year_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staging',
            name='month_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staging',
            name='year_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
