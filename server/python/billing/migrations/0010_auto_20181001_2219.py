# Generated by Django 2.0 on 2018-10-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0009_timeentry_time_entry_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmatter',
            name='is_matter_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matter',
            name='is_matter_paid',
            field=models.BooleanField(default=False),
        ),
    ]
