# Generated by Django 4.2 on 2023-06-03 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord', '0003_alter_discorduser_discord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discorduser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]