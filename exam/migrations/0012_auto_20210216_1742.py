# Generated by Django 2.2.7 on 2021-02-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20200110_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='end_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='start_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]