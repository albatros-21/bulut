# Generated by Django 2.2.7 on 2019-11-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_choice_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('qs_id', models.IntegerField()),
                ('choice_id', models.IntegerField()),
                ('exam_id', models.IntegerField()),
            ],
        ),
    ]