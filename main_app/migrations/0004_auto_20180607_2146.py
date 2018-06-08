# Generated by Django 2.0.6 on 2018-06-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20180607_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='lat',
            field=models.DecimalField(decimal_places=13, default=0.0, max_digits=13),
        ),
        migrations.AddField(
            model_name='destination',
            name='long',
            field=models.DecimalField(decimal_places=13, default=0.0, max_digits=13),
        ),
    ]
