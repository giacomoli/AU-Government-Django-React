# Generated by Django 2.0 on 2018-08-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_industry_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='xero_branding_theme_id',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
