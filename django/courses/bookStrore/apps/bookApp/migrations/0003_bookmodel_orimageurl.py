# Generated by Django 5.0.4 on 2024-04-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0002_bookmodel_bookimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='orImageUrl',
            field=models.URLField(null=True, verbose_name='Or Image URL'),
        ),
    ]
