# Generated by Django 3.2.9 on 2021-12-05 16:44

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_image_image_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='postee',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='postee',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='pictures'),
        ),
    ]