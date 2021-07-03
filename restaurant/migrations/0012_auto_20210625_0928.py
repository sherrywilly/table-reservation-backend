# Generated by Django 3.1.7 on 2021-06-25 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_auto_20210623_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Location name'),
        ),
    ]
