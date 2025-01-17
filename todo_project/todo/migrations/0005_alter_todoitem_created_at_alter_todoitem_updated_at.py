# Generated by Django 5.0.4 on 2024-04-06 14:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todoitem_created_at_todoitem_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='updated_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
