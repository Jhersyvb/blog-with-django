# Generated by Django 2.2.7 on 2019-11-28 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20191126_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]