# Generated by Django 4.0.4 on 2022-05-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0004_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_circle',
            field=models.BooleanField(default=False, verbose_name='کامپوننت آن دایره ای باشد؟'),
        ),
    ]
