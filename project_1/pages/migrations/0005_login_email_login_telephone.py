# Generated by Django 4.0.4 on 2022-08-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_login_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(default='00000@naver.com', max_length=254),
        ),
        migrations.AddField(
            model_name='login',
            name='telephone',
            field=models.IntegerField(default='010-0000-0000'),
        ),
    ]
