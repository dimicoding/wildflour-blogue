# Generated by Django 3.2.18 on 2023-05-02 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230426_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='slug',
        ),
    ]
