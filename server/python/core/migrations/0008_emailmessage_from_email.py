# Generated by Django 2.0 on 2018-09-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180817_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='from_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
