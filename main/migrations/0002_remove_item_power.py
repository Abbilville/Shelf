# Generated by Django 4.2.4 on 2023-09-10 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='power',
        ),
    ]
