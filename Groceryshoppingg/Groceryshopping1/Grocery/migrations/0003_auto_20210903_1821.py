# Generated by Django 3.1.7 on 2021-09-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery', '0002_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
