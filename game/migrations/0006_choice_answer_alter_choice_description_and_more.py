# Generated by Django 5.1.3 on 2024-11-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_question_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='choice',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question_id',
            field=models.IntegerField(default=''),
        ),
    ]