# Generated by Django 2.0.6 on 2018-06-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_destination_adventure'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='apr',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='aug',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='beach',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destination',
            name='dec',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='feb',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='jan',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='jul',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='jun',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='mar',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='may',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='nov',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='oct',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='sep',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='destination',
            name='ski',
            field=models.BooleanField(default=False),
        ),
    ]