# Generated by Django 5.0.4 on 2024-04-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='bookImage',
            field=models.ImageField(null=True, upload_to='bookImages', verbose_name='Book Image'),
        ),
    ]