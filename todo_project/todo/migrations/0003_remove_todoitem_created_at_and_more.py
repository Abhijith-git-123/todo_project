# Generated by Django 5.0.4 on 2024-04-06 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todoitem_completed_remove_todoitem_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='updated_at',
        ),
    ]
