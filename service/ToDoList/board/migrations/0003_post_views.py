# Generated by Django 5.0.6 on 2024-07-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0002_post_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]