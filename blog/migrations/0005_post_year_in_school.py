# Generated by Django 2.1.1 on 2018-11-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181129_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
