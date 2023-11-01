# Generated by Django 4.2.6 on 2023-10-31 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0009_rename_habit_taskmodel_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitmodel',
            name='level',
        ),
        migrations.RemoveField(
            model_name='habitmodel',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='habitmodel',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='habitmodel',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='habitmodel',
            name='tree_id',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='level',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='habit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='habits.habitmodel'),
            preserve_default=False,
        ),
    ]
