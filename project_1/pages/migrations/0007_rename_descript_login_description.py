# Generated by Django 4.0.4 on 2022-08-31 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_login_telephone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='descript',
            new_name='description',
        ),
    ]
