# Generated by Django 3.0.8 on 2020-07-21 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200721_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='winner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]
