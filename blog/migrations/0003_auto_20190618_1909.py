# Generated by Django 2.0.6 on 2019-06-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
