# Generated by Django 3.0.8 on 2020-08-11 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200811_0924'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bids',
        ),
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
