# Generated by Django 5.0.7 on 2024-09-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_usersdetails_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdetails',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
