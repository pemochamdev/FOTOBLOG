# Generated by Django 4.2.7 on 2023-11-04 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_word_content_blog_word_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='word_count',
            field=models.IntegerField(null=True),
        ),
    ]