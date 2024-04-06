# Generated by Django 5.0.4 on 2024-04-06 14:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_remove_todoitem_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
