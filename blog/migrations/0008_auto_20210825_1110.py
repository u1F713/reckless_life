# Generated by Django 3.2.6 on 2021-08-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_projectpost_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectposttag',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='projectposttag',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ArticleTag',
        ),
        migrations.DeleteModel(
            name='ProjectPostTag',
        ),
    ]
