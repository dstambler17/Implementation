# Generated by Django 2.0.6 on 2019-06-19 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_podcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='slug',
            field=models.SlugField(default='Please enter here', max_length=100),
        ),
    ]
