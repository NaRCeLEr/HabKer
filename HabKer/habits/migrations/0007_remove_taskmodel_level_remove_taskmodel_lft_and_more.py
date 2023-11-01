# Generated by Django 4.2.6 on 2023-10-31 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_remove_taskmodel_parent_habitmodel_parent_and_more'),
    ]

    operations = [
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
            name='rght',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='habitmodel',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habitmodel',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habitmodel',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habitmodel',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]