# Generated by Django 5.0.4 on 2024-04-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0005_alter_reviewsmodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating',
            field=models.IntegerField(default=1, null=True, verbose_name='Rating'),
        ),
    ]
