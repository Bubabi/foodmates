# Generated by Django 2.1 on 2018-09-05 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_condition_yenifield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='yenifield',
        ),
    ]
