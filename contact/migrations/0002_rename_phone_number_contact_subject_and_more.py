# Generated by Django 4.2.3 on 2023-07-16 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
