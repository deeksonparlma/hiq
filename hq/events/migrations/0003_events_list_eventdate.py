# Generated by Django 3.0 on 2020-01-18 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200118_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='events_list',
            name='eventDate',
            field=models.DateField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]