# Generated by Django 3.2.8 on 2021-10-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUs', '0002_auto_20210415_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]