# Generated by Django 3.1.3 on 2020-11-11 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='titlezipcode',
            new_name='zipcode',
        ),
    ]
