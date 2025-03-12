# Generated by Django 5.1.6 on 2025-03-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('user', 'User')], default='user', max_length=10),
        ),
    ]
