# Generated by Django 3.2.5 on 2021-07-14 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_register_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='type',
        ),
    ]
