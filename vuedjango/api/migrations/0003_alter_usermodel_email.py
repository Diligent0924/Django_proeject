# Generated by Django 4.0.4 on 2022-10-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_usermodel_username_usermodel_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
