# Generated by Django 3.1.2 on 2020-10-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxima_exped', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='date',
            field=models.DateField(),
        ),
    ]
