# Generated by Django 3.2.9 on 2022-01-25 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]