# Generated by Django 3.1.6 on 2021-02-05 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snowflake_instances', '0002_instances_last_connected'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rule_engine', '0010_auto_20210205_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='donotnotifyusers',
            name='instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snowflake_instances.instances'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='donotnotifyusers',
            unique_together={('instance', 'user')},
        ),
        migrations.RemoveField(
            model_name='donotnotifyusers',
            name='audit',
        ),
    ]
