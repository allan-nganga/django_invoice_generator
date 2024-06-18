# Generated by Django 5.0.6 on 2024-06-14 16:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing_app', '0004_alter_client_client_country_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
