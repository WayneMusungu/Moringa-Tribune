# Generated by Django 4.0.4 on 2022-05-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_tags_editor_phone_number_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=True, upload_to='articles/'),
        ),
    ]
