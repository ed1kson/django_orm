# Generated by Django 5.0.1 on 2024-01-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0006_alter_game_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.FloatField(),
        ),
    ]