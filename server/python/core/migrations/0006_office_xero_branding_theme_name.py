# Generated by Django 2.0 on 2018-08-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_matterstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='xero_branding_theme_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
