# Generated by Django 3.2.5 on 2021-07-24 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0003_auto_20210720_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='where',
            field=models.TextField(default=''),
        ),
    ]
