# Generated by Django 5.0.6 on 2024-06-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_country',
            field=models.TextField(blank=True, null=True),
        ),
    ]