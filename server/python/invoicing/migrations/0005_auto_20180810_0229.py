# Generated by Django 2.0 on 2018-08-10 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0004_auto_20180808_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpayment',
            name='xero_payment_id',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='xero_payment_id',
            field=models.CharField(max_length=256, null=True),
        ),
    ]