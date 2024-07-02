# Generated by Django 4.2 on 2023-08-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_remove_team_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='main_picture',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='line_images', verbose_name='фотография 390x500px'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='corporate_structure_picture',
            field=models.ImageField(blank=True, null=True, upload_to='team_images', verbose_name='фотография структуры 2000x840px'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to='team_images', verbose_name='главная фотография 2000x840px'),
        ),
    ]
