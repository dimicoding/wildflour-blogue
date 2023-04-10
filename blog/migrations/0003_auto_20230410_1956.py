# Generated by Django 3.2.18 on 2023-04-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_recipe_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='dificulty',
            field=models.IntegerField(choices=[(0, 'Easy'), (1, 'Medium'), (2, 'Hard')], default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_time',
            field=models.IntegerField(default=60),
        ),
    ]
