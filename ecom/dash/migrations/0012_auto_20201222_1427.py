# Generated by Django 3.1.1 on 2020-12-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_product_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(blank=True, default='bottle.jpg', null=True, upload_to=''),
        ),
    ]
