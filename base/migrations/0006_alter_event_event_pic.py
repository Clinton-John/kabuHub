# Generated by Django 5.0 on 2024-02-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_event_event_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_pic',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=''),
        ),
    ]