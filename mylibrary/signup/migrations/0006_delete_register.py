# Generated by Django 3.2.5 on 2021-07-14 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_remove_register_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
    ]
