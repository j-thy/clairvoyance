# Generated by Django 4.2.9 on 2024-01-06 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banners_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='image',
            new_name='image_file',
        ),
    ]