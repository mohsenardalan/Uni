# Generated by Django 3.0.6 on 2020-05-26 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0005_auto_20200525_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_field',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_phone',
            field=models.CharField(default=' ', max_length=11),
            preserve_default=False,
        ),
    ]
