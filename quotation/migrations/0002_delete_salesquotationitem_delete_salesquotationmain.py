# Generated by Django 5.1 on 2024-08-25 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SalesQuotationItem',
        ),
        migrations.DeleteModel(
            name='SalesQuotationMain',
        ),
    ]
