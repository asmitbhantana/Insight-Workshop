# Generated by Django 3.0.8 on 2020-07-19 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20200719_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]