# Generated by Django 3.1.2 on 2020-10-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowflake_connector', '0002_auto_20201030_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='instances',
            name='instance_account',
            field=models.CharField(default='null', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]