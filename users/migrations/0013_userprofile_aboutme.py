# Generated by Django 3.0.5 on 2020-06-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200513_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='aboutMe',
            field=models.TextField(default=''),
        ),
    ]
