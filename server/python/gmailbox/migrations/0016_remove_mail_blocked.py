# Generated by Django 2.0 on 2019-01-16 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmailbox', '0015_mail_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='blocked',
        ),
    ]
