# Generated by Django 4.2 on 2023-07-25 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('line', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=265, verbose_name='название')),
                ('title_ru', models.CharField(max_length=265, null=True, verbose_name='название')),
                ('title_ky', models.CharField(max_length=265, null=True, verbose_name='название')),
                ('title_en', models.CharField(max_length=265, null=True, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('description_ru', models.TextField(null=True, verbose_name='описание')),
                ('description_ky', models.TextField(null=True, verbose_name='описание')),
                ('description_en', models.TextField(null=True, verbose_name='описание')),
                ('file', models.ImageField(blank=True, null=True, upload_to='project_images', verbose_name='фотография')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='год')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='line.line', verbose_name='направление')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.CreateModel(
            name='ExtraFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='line_images', verbose_name='фотография проекта')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extrafields', to='project.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'экстра поле',
                'verbose_name_plural': 'экстра поля',
            },
        ),
    ]