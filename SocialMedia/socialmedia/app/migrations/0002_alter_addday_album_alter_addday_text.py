# Generated by Django 4.0.4 on 2022-05-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addday',
            name='album',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='addday',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
