# Generated by Django 4.2 on 2023-09-06 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_postpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postpage',
            options={'verbose_name': 'фон для новостей', 'verbose_name_plural': 'фон для новостей'},
        ),
    ]