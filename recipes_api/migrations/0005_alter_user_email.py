# Generated by Django 4.1.3 on 2022-11-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_api', '0004_alter_favorite_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]