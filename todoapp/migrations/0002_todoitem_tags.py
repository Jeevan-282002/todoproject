# Generated by Django 4.2.2 on 2023-06-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='tags',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
