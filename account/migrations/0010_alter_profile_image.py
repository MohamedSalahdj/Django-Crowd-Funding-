# Generated by Django 4.2 on 2024-03-06 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='account/images/'),
        ),
    ]
