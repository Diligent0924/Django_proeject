# Generated by Django 4.0.4 on 2022-09-13 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articlemodel_update_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalModel',
        ),
    ]
