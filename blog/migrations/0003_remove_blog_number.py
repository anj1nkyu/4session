# Generated by Django 4.1.7 on 2023-03-27 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='number',
        ),
    ]