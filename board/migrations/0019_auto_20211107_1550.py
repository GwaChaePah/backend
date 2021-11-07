# Generated by Django 3.2.8 on 2021-11-07 15:50

import board.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0018_alter_post_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(upload_to=board.models.post_directory_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=board.models.post_directory_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=board.models.post_directory_path),
        ),
    ]
