# Generated by Django 4.1.5 on 2023-01-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_tags_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.tag'),
        ),
    ]