# Generated by Django 3.0 on 2020-01-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200118_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events_list',
            old_name='event_organizerid',
            new_name='event_organizer',
        ),
    ]
