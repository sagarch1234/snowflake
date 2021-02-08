# Generated by Django 3.1.6 on 2021-02-06 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine', '0012_auditrecommendedarticles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppliedRule',
            new_name='ApplicableRule',
        ),
        migrations.RenameField(
            model_name='auditrecommendedarticles',
            old_name='article',
            new_name='article_links',
        ),
        migrations.AlterField(
            model_name='auditrecommendedarticles',
            name='audit_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_recommended_article', to='rule_engine.auditsresults'),
        ),
    ]