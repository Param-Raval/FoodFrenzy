# Generated by Django 2.2.12 on 2020-05-13 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodspark', '0002_auto_20200513_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryitem',
            old_name='deliveryboy',
            new_name='deliveryboy_id',
        ),
    ]
