# Generated by Django 2.1.1 on 2018-11-30 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='year_in_school',
        ),
    ]
