# Generated by Django 2.2.3 on 2019-08-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
