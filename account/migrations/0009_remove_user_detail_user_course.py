# Generated by Django 4.0.1 on 2022-02-14 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_detail_user_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_detail',
            name='user_course',
        ),
    ]
