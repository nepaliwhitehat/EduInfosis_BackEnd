# Generated by Django 2.1.5 on 2019-02-18 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0012_auto_20190217_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentpayment',
            name='receipt_number',
        ),
    ]
