# Generated by Django 5.0.6 on 2024-06-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework4', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
