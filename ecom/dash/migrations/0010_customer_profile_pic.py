# Generated by Django 3.1.1 on 2020-12-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_auto_20201218_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
