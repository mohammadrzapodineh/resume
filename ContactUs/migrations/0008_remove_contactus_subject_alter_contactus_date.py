# Generated by Django 4.0.4 on 2022-05-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUs', '0007_alter_contactus_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='subject',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ'),
        ),
    ]
