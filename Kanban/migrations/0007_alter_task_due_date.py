# Generated by Django 4.0.6 on 2023-03-02 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0006_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]