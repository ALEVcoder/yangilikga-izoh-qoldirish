# Generated by Django 4.0.3 on 2022-03-07 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='news'),
            preserve_default=False,
        ),
    ]