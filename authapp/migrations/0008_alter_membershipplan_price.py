# Generated by Django 4.2.3 on 2023-07-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_trainer_timestamp_alter_membershipplan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.IntegerField(),
        ),
    ]
