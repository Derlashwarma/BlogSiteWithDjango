# Generated by Django 5.0.6 on 2024-06-10 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
