# Generated by Django 4.0.6 on 2023-05-06 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0010_remove_subtask_description_remove_task_subtask_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(related_name='tasks', to='Kanban.subtask'),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks_set', to='Kanban.task'),
        ),
    ]
