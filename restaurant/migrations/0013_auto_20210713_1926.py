# Generated by Django 3.1.7 on 2021-07-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_auto_20210625_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='seatingCapacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
