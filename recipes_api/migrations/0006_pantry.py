# Generated by Django 4.1.3 on 2022-11-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_api', '0005_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pantry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
