# Generated by Django 3.1.2 on 2020-10-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
