# Generated by Django 5.0.1 on 2024-01-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category_name',
        ),
        migrations.AddField(
            model_name='article',
            name='category_name',
            field=models.ManyToManyField(null=True, to='articles.category'),
        ),
    ]
