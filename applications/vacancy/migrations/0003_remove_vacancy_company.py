# Generated by Django 4.2 on 2023-08-09 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_alter_vacancy_main_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='company',
        ),
    ]