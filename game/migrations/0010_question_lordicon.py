# Generated by Django 5.1.3 on 2024-11-23 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_type_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='lordicon',
            field=models.TextField(default=''),
        ),
    ]
