# Generated by Django 3.2.6 on 2022-05-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='admin', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='mail@mail.com', max_length=64),
            preserve_default=False,
        ),
    ]