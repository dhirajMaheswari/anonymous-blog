# Generated by Django 2.1.1 on 2018-12-07 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]