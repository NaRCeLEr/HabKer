# Generated by Django 4.2.6 on 2023-10-31 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0008_taskmodel_level_taskmodel_lft_taskmodel_rght_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='habit',
            new_name='parent',
        ),
    ]