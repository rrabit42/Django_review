# Generated by Django 2.2.3 on 2019-08-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]
