# Generated by Django 3.1.7 on 2021-03-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20210327_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
