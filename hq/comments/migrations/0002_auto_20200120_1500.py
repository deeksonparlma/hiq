# Generated by Django 3.0 on 2020-01-20 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment_list',
            table='comments',
        ),
    ]