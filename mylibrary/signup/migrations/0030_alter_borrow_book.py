# Generated by Django 3.2.5 on 2021-07-19 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0029_remove_borrow_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(default='book', on_delete=django.db.models.deletion.CASCADE, to='signup.book'),
        ),
    ]
