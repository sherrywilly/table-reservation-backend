# Generated by Django 3.1.5 on 2021-01-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='categorys',
            field=models.ManyToManyField(blank=True, limit_choices_to=2, null=True, to='restaurant.RestCategory'),
        ),
    ]