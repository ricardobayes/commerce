# Generated by Django 3.0.8 on 2020-07-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200720_2232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bids',
            options={'verbose_name_plural': 'Bids'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='listings',
            options={'verbose_name_plural': 'Listings'},
        ),
        migrations.AlterModelOptions(
            name='watchlist',
            options={'verbose_name_plural': 'Watchlist'},
        ),
        migrations.AddField(
            model_name='listings',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]