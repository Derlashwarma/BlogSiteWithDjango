# Generated by Django 5.0.6 on 2024-06-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='null', upload_to='blog/images/'),
            preserve_default=False,
        ),
    ]
