# Generated by Django 3.1.7 on 2021-05-31 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20210531_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
