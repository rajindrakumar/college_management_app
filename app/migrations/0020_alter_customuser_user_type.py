# Generated by Django 3.2.24 on 2024-02-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'STUDENT'), (1, 'HOD'), (2, 'STAFF')], default=1, max_length=50),
        ),
    ]
