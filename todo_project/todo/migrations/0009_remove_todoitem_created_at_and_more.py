# Generated by Django 5.0.4 on 2024-04-06 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_alter_todoitem_created_at_alter_todoitem_updated_at'),
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
