# Generated by Django 5.0 on 2024-02-23 20:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_event_event_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=128, unique=True)),
                ('points', models.IntegerField(default=0)),
                ('goals_scored', models.IntegerField(default=0)),
                ('goals_against', models.IntegerField(default=0)),
                ('goal_difference', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Sport_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('sports_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('venue', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
