# Generated by Django 4.2.3 on 2023-07-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_membershipplan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.IntegerField(),
        ),
    ]
