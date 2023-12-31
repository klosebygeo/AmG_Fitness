# Generated by Django 4.2.3 on 2023-07-17 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authapp', '0009_alter_enrollment_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='FullName',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
