# Generated by Django 4.0.6 on 2023-07-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0016_alter_task_category_alter_task_urgency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Management', 'MANAGEMENT'), ('Sales', 'SALES'), ('Marketing', 'MARKETING'), ('Product', 'PRODUCT')], default='Management', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='urgency',
            field=models.CharField(choices=[('High', 'HIGH'), ('Mid', 'MEDIUM'), ('Low', 'LOW')], default='High', max_length=10),
        ),
    ]
