# Generated by Django 3.2.8 on 2021-11-07 15:11

import board.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_auto_20211107_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(upload_to=board.models.post_directory_path),
        ),
    ]
