# Generated by Django 5.1.7 on 2025-05-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Character', '0015_alter_hero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.ImageField(blank=True, default='media/Kiriko_Overwatch.png', null=True, upload_to='image'),
        ),
    ]
