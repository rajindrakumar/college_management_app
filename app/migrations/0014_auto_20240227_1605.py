# Generated by Django 3.2.24 on 2024-02-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20240227_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (3, 'STUDENT'), (2, 'STAFF')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='staff_feedback',
            name='feedback_reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
