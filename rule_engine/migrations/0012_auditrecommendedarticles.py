# Generated by Django 3.1.6 on 2021-02-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine', '0011_auto_20210205_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditRecommendedArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('article', models.TextField(blank=True, null=True)),
                ('audit_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rule_engine.auditsresults')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]