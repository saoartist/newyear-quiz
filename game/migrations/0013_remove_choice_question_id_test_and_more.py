# Generated by Django 5.1.3 on 2024-11-25 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_choice_question_id_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question_id_test',
        ),
        migrations.AlterField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='game.question'),
        ),
    ]
