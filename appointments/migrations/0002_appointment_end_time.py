# Generated by Django 4.1.2 on 2024-01-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
