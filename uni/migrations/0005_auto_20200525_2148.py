# Generated by Django 3.0.6 on 2020-05-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0004_auto_20200525_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Admin_username',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_username',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]