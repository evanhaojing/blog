# Generated by Django 2.1.5 on 2019-01-15 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='username',
        ),
    ]
