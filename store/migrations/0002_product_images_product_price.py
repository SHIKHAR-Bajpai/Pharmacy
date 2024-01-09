# Generated by Django 4.1.6 on 2023-02-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default='', upload_to='store/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
