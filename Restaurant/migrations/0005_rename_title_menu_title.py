# Generated by Django 5.1.4 on 2025-01-15 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Title',
            new_name='title',
        ),
    ]
