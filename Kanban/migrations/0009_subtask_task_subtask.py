# Generated by Django 4.0.6 on 2023-04-29 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0008_alter_myuser_password_alter_task_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('completion_status', models.BooleanField(default=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='Kanban.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='subtask',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_task', to='Kanban.subtask'),
        ),
    ]