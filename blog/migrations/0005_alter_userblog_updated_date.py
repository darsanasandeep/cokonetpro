# Generated by Django 4.1.2 on 2022-12-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_userblog_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]
