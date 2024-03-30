# Generated by Django 3.2.24 on 2024-02-27 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20240227_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, default='DEFAULT VALUE', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('student_id', models.ForeignKey(blank=True, default='DEFAULT VALUE', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
