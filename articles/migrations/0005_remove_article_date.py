# Generated by Django 5.0.1 on 2024-01-28 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_category_name_article_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]
