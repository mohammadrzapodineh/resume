# Generated by Django 4.0.4 on 2022-05-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='avatar',
            field=models.ImageField(default=1, upload_to='avatar/', verbose_name='آواتار'),
            preserve_default=False,
        ),
    ]
