# Generated by Django 5.1.7 on 2025-04-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('tier', models.CharField(max_length=50)),
            ],
        ),
    ]
