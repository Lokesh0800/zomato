# Generated by Django 4.0.5 on 2022-12-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboy',
            name='enp_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='deliveryboy',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
    ]
