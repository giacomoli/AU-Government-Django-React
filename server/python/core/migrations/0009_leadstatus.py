# Generated by Django 2.0 on 2018-09-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_emailmessage_from_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Lead statuses',
            },
        ),
    ]
