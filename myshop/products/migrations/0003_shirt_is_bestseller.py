# Generated by Django 4.2.4 on 2023-08-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_shirt_brand_shirt_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
    ]