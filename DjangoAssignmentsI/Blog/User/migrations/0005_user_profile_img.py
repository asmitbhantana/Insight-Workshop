# Generated by Django 3.0.8 on 2020-07-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20200719_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='default-img.png', upload_to=''),
        ),
    ]
