# Generated by Django 4.2.3 on 2023-07-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_alter_membershipplan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='Address',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
