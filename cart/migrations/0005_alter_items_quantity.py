# Generated by Django 4.2.7 on 2023-12-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_items_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
