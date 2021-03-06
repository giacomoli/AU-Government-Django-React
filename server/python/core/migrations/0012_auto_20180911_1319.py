# Generated by Django 2.0 on 2018-09-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_accountnumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountnumber',
            options={'ordering': ('entry_type',), 'verbose_name_plural': 'Account numbers'},
        ),
        migrations.AlterField(
            model_name='accountnumber',
            name='account_number',
            field=models.IntegerField(default=200),
        ),
    ]
