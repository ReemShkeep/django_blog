# Generated by Django 4.0.2 on 2022-02-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=models.CharField(max_length=2000),
        ),
    ]
