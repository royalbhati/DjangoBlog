# Generated by Django 2.1 on 2019-06-11 06:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190611_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hearts',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]