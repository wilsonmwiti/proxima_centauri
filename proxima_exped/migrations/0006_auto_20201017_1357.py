# Generated by Django 3.1.2 on 2020-10-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxima_exped', '0005_expedition_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedition',
            name='account_name',
            field=models.CharField(default='PROXIMA', max_length=24),
        ),
        migrations.AddField(
            model_name='expedition',
            name='account_no',
            field=models.IntegerField(default=30157),
        ),
        migrations.AddField(
            model_name='expedition',
            name='inclusives',
            field=models.TextField(default='Transport, Water'),
        ),
        migrations.AddField(
            model_name='expedition',
            name='person_price',
            field=models.FloatField(default=0.0),
        ),
    ]