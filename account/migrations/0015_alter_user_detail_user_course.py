# Generated by Django 4.0.1 on 2022-03-02 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_release_date'),
        ('account', '0014_alter_user_detail_user_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='user_course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
            preserve_default=False,
        ),
    ]