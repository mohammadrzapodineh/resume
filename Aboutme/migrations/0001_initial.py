# Generated by Django 4.0.4 on 2022-05-02 17:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')),
                ('location', models.CharField(max_length=120, verbose_name='محل سکونت')),
                ('biography', ckeditor.fields.RichTextField(verbose_name='بیوگرافی')),
                ('success_projects', models.IntegerField(default=0, verbose_name='تعداد پروژه های موفق')),
                ('work_experience', models.IntegerField(default=0, verbose_name='سابقه کار')),
            ],
            options={
                'verbose_name': 'درباره من',
                'verbose_name_plural': 'درباره های من',
            },
        ),
    ]