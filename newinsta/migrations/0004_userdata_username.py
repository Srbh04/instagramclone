# Generated by Django 3.1.1 on 2020-09-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newinsta', '0003_userdata_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
