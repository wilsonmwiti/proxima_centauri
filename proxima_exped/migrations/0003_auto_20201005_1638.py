# Generated by Django 3.1.2 on 2020-10-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxima_exped', '0002_auto_20201005_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='expedition/images/'),
        ),
    ]
