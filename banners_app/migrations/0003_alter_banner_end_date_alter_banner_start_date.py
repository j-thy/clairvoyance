# Generated by Django 4.2.9 on 2024-01-06 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners_app', '0002_rename_image_event_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]