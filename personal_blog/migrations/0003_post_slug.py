# Generated by Django 5.0.7 on 2025-01-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0002_rename_text_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default-slug', unique=False),
        ),
    ]
