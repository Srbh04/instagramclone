# Generated by Django 3.1.1 on 2020-09-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newinsta', '0004_userdata_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='image',
            field=models.ImageField(default=' ', upload_to='images/'),
            preserve_default=False,
        ),
    ]
