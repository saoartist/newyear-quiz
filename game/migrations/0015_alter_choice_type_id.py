# Generated by Django 5.1.3 on 2024-11-25 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_choice_type_id_alter_choice_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='type_choices', to='game.type'),
        ),
    ]
